from Scheduler import Scheduler

# Modify Class Data and Work Schedule
# class1 = ['PHYS16','MWF:12-13','TuWTh:15-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','MW:15-19',8,'Th:18',0.30]
# class3 = ['GENED1023','TuTh:12-14','MW:12-13',2,'W:18',0.15]
work_ = 'MTuWThF:12-18'

# Do not Modify
D = Scheduler()
# S.add_class(class1)
D.add_class(class2)
# S.add_class(class3)
D.add_work_schedule(work_)
D.add_constraints(1,5)
F = D.back_tracking_search()
D.print_final_schedule(F)
