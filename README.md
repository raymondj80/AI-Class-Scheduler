# AI-Class-Scheduler

AI Scheduler that uses a CSP and MDP model to determine the optimal schedule for a college student taking classes.

## Getting Started

### Prerequisites

```
pip install numpy
```

### Installing

Clone the Github repo

```
git clone https://github.com/raymondj80/AI-Class-Scheduler.git
cd AI-Class-Scheduler
```

### Loading Schedulers

For the CSP Scheduler (Approach 1)

```
cd Approach1
```

For the MDP Scheduler (Approach 2)

```
cd Approach2
```

## Running the tests

Inputting class data and work schedule \
class = [class_name, class_hours, office_hours, difficulty, hw_deadline, hw_weight]

```
class1 = ['PHYS16','MWF:12-13','TuWTh:15-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','MW:15-19',8,'Th:18',0.15]
class3 = ['GENED1023','TuTh:12-14','MW:12-13',2,'W:18',0.15]
work_ = 'MTuWThFSatSun:12-20'
```

### Running Scheduler 
For the CSP Scheduler (Approach 1)
```
from Scheduler import Scheduler
S = Scheduler()
S.add_class(class1)
S.add_class(class2)
S.add_class(class3)
S.add_work_schedule(work_)
S.add_constraints(0,5)
F = S.back_tracking_search()
S.print_final_schedule(F)
```

For the MDP Scheduler (Approach 2)
```
from MScheduler import MScheduler
MS = MScheduler()
MS.add_class(class1)
MS.add_class(class2)
MS.add_class(class3)
MS.add_work_schedule(work_)
MS.maximize_utility()
MS.print_final_schedule()
```

### Additionally there are SchedulerRunner.py files to run the scheduler
```
python SchedulerRunnner.py
```

```
python MSchedulerRunnner.py
```

      
