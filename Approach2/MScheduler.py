"Written by Raymond Jow V2.0 2020"

from MarkovClass import MarkovClass
from MTimeSlot import MTimeSlot
import matplotlib.pyplot as plt

class MScheduler:
    def __init__(self):
        self.classList = []
        self.work_schedule = []
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
            self.work_schedule.append(time_slot)

    def add_class(self,class_data):
        new_class = MarkovClass(class_data[0], self.parseHours(class_data[1]), self.parseHours(class_data[2]), class_data[3], self.parseHours(class_data[4]),class_data[5])
        new_class.value_Iteration(0.9,0.1)
        self.classList.append(new_class)

    def maximize_utility(self):
        "Iterates through timeslots in partition and returns timeslot with max utility"
        for timeslot in self.work_schedule:
            # Get valid actions
            valid_actions = timeslot.get_valid_actions(self.classList)
            # Calculate the utility of each time slot
            timeslot.calc_utility(valid_actions)
            timeslot.updateState(self.classList)
             
    def print_final_schedule(self):
        "Prints a formatted table with the time, class, action, utility, and work done"
        for timeslot in self.work_schedule:
            best_class = timeslot.max_class.name
            best_action = timeslot.max_action
            time = self.timeToString(timeslot.time)
            utility = timeslot.utility
            work_done = timeslot.work_done/100
            fatigue = timeslot.fatigue
            proficiency = timeslot.proficiency
            print("Time: {: <9} Class: {: <13} Action: {: <10} Utility: {: <10.2f} Work Done: {: <10.0%} Fatigue: {: <9} Proficiency: {: <10.0%}".format(time, best_class, best_action, utility, work_done, fatigue, proficiency))

    def timeToString(self,time):
        day = ['Sun', 'M', 'Tu', 'W', 'Th', 'F', 'Sat'][time // 24]
        hour = time % 24
        return "{}:{}".format(day,hour)
