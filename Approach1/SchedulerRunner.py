from Scheduler import Scheduler

"""
Python file that runs the Scheduler class
-----------------------------------------
Modify Class Data, Work Schedule, and Constraints
"""

# Modify Class Data and Work Schedule
class1 = ['PHYS16','MWF:12-16','MWTh:13-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','TuTh:18-19',4,'W:12',0.30]
class3 = ['GENED1023','TuTh:12-14','MW:12-13',1,'W:18',0.15]
work_ = 'MTuWThF:12-18'

# Modify Constraints (break_hours_between_work, total_work_hours_per_day)
S = Scheduler()
S.add_constraints(1,5)

# Do not Modify
S.add_class(class1)
S.add_class(class2)
S.add_class(class3)
S.add_work_schedule(work_)
F = S.back_tracking_search()
S.print_final_schedule(F)
