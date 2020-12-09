import numpy as np

class Class:
    """
    Class used to represent a class that the student is taking in the CSP Model
    
    Atrtributes
    -----------
    name: string
        name of class
    deadline: int
        hour of deadline (0-168)
    weight: float
        weight of homework(0-1)
    class_times: int array
        list of class times
    oh_times: int array
        list of oh times
    bt_time: np.array
        Used by backtrack algorithm
        [total_class_hours, total_oh_hours, total_work_hours]
    time:
        Used to recalculate utility after bt
        [total_class_hours, total_oh_hours, total_work_hours]
    """
    
    def __init__(self,class_name,class_times,oh_times,difficulty,pset_deadline,pset_weight):
        self.name = class_name
        self.deadline = pset_deadline[0]
        self.difficulty = difficulty
        self.weight = pset_weight
        self.class_times = class_times
        self.oh_times = oh_times
        self.bt_time = np.array([0,0,0])
        self.time = np.array([0,0,0])

    def update(self,action,bt=False):
        "set the time vector"
        if bt:
            self.bt_time = self.bt_time + action
        else:
            self.time = self.time + action
            
    def getTimeVec(self,bt=False):
        "get the time vector"
        if bt:
            return self.bt_time
        else:
            return self.time








    






