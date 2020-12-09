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

There are SchedulerRunner.py files to run the Scheduler 

For the CSP Scheduler (Approach 1)
```
python SchedulerRunnner.py
```

For the MDP Scheduler (Approach 2)
```
python MSchedulerRunnner.py
```

Inside the SchedulerRunner.py files, you can modify the class data and work schedule \
Inputting class data and work schedule \
class = [class_name, class_hours, office_hours, difficulty, hw_deadline, hw_weight] \
work_schedule = 'Days:StartHour-EndHour' \
The Symbols for each day are as follows: \
Monday:M, Tuesday:Tu, Wednesday:W, Thursday:Th, Friday:F, Saturday:Sat, Sunday:Sun


Example:
```
class1 = ['PHYS16','MWF:12-13','TuWTh:15-18',6,'F:18',0.30]
class2 = ['CS182','MWF:14-15','MW:15-19',8,'Th:18',0.15]
class3 = ['GENED1023','TuTh:12-14','MW:12-13',2,'W:18',0.15]
work_ = 'MTuWThFSatSun:12-20'
```
Additionally, for the CSP Scheduler, you can change the constraints \
The format for the constraints is the following: \
add_constraints(break_hours_between_work, total_work_hours_per_day)

Example: \

1 break_hours_between_work, 5 total_work_hours_per_day 
```
S.add_constraints(1,5)
```





      
