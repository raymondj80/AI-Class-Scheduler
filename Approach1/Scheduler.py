from Class import Class
from TimeSlot import TimeSlot
import copy

class Scheduler:
    def __init__(self):
        self.classList = []
        self.work_schedule = [[] for i in range(7)]
        self.constraints = None
        self.hours = [i for i in range(168)]
        self.max_hours = []

    def parseHours(self,hours):
        times_list = []
        times = hours.split(',')
        for t in times:
            day, hour = t.split(':')
            if '-' in hour:
                hours = range(int(hour.split('-')[0]),int(hour.split('-')[1]))
            else:
                hours = [hour]
            for h in hours:
                if 'Sun' in day:
                    times_list.append(int(h))
                if 'M' in day:
                    times_list.append(24 + int(h))
                if 'Tu' in day:
                    times_list.append(48 + int(h))
                if 'W' in day:
                    times_list.append(72 + int(h))
                if 'Th' in day:
                    times_list.append(96 + int(h))
                if 'F' in day:
                    times_list.append(120 + int(h))
                if 'Sat' in day:
                    times_list.append(144 + int(h))
        return sorted(times_list)

    def add_work_schedule(self,work_schedule):
        "adds work schedule to instance variable work_schedule"
        self.work_hours = self.parseHours(work_schedule)
        for work_hour in self.work_hours:
            time_slot = TimeSlot(work_hour)
            self.work_schedule[time_slot.time // 24].append(time_slot)

    def add_class(self,class_data):
        new_class = Class(class_data[0], self.parseHours(class_data[1]), self.parseHours(class_data[2]), class_data[3], self.parseHours(class_data[4]),class_data[5])
        self.classList.append(new_class)

    def add_constraints(self,work_hour_intervals, work_hours_per_day):
        "Adds constraints to instance variable constraints"
        self.constraints = (work_hour_intervals, work_hours_per_day)

    def maximize_utility(self,partition):
        "Iterates through timeslots in partition and returns timeslot with max utility"
        for timeslot in partition:
            # Get valid actions
            valid_actions = timeslot.get_valid_actions(self.classList)
            # Calculate the utility of each time slot
            timeslot.calc_utility(valid_actions,bt=True)
            # Get the timeslot with highest utility
        max_timeslot = max(partition, key=lambda partition: partition.utility)
            # Return the best timeslot
        return max_timeslot
    
    def back_tracking_search(self):
        "Back tracking search for CSP, returns the best schedule given constraints"
        max_schedule = []
        for partition in self.work_schedule:
            max_partition = sorted(self.back_track(partition),key=lambda timeslot: timeslot.time,reverse=False)
            # Recalculate the utility once the best timeslots are selected
            for idx,timeslot in enumerate(max_partition):
                timeslot.calc_utility([[timeslot.max_class,timeslot.max_action]],bt=False)
                timeslot.max_class.update(timeslot.max_action,False)
                timeslot.update_pset(self.classList)

            max_schedule.append(max_partition)
        return max_schedule

    def back_track(self,partition):
        "Returns list of timeslots that maximize utility and satisfy constraints"
        break_hours, total_work_hours = self.constraints
        # Base case
        if len(partition) == 0:
            return []
        else:
            # Calculate the utilities of remaining timeslots and update
            max_timeslot = self.maximize_utility(partition)
            max_timeslot.max_class.update(max_timeslot.max_action,True)
            partition.remove(max_timeslot)
            # Removes timeslots that do not satisfy constraints
            partition_copy = partition.copy()
            for p in partition_copy:
                if (abs(p.time - max_timeslot.time) <= break_hours):
                    partition.remove(p)
            # Recurse
            return ([max_timeslot] + self.back_track(partition))[:total_work_hours]
             
    def print_final_schedule(self,back_track):
        "Prints a formatted table with the time, class, action, utility, and work done"
        for day in back_track:
            for timeslot in day:
                best_class = timeslot.max_class.name
                best_action = self.actionToString(timeslot.max_action)
                time = self.timeToString(timeslot.time)
                utility = timeslot.utility
                work_done = timeslot.work_done
                print("Time: {: <9} Class: {: <13} Action: {: <10} Utility: {: <10.3f} Work Done: {}".format(time, best_class, best_action, utility, work_done))

    def actionToString(self,action):
        "Converts action array to string"
        return ['class', 'OH', 'work'][list(action).index(1)] 

    def timeToString(self,time):
        day = ['Sun', 'M', 'Tu', 'W', 'Th', 'F', 'Sat'][time // 24] 
        hour = time % 24
        return "{}:{}".format(day,hour)

# Test Case 3
class1 = ['PHYS16','MWF:12-13','TuWTh:15-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','MW:15-19',8,'Th:18',0.15]
class3 = ['GENED1023','TuTh:12-14','MW:12-13',2,'W:18',0.15]
work_ = 'MTuWThFSatSun:12-20'







