from MScheduler import MScheduler

# Modify Class Data and Work Schedule
class1 = ['PHYS16','MWF:12-16','MWTh:13-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','MW:15-19',2,'Th:18',0.30]
class3 = ['GENED1023','TuTh:12-14','MW:12-13',1,'W:18',0.15]
work_ = 'MTuWThFSatSun:12-19'

# Do not Modify
MS = MScheduler()
MS.add_class(class1)
MS.add_class(class2)
MS.add_class(class3)
MS.add_work_schedule(work_)
MS.maximize_utility()
MS.print_final_schedule()