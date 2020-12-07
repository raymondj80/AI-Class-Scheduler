import numpy as np

class My_Class:
    OH = 0.5
    def __init__(self,class_name,class_times,oh_times,difficulty,pset_deadline,pset_weight):
        self.name = class_name
        self.deadline = pset_deadline[0]
        self.difficulty = difficulty
        self.weight = pset_weight
        self.class_times = class_times
        self.oh_times = oh_times
        self.bt_time = np.array([0,0,0])
        self.time = np.array([0,0,0])
        self.E_pset = []
        self.W_pset = []
        self.update_prev = 0
        
    # set the time vector
    def update(self,action,bt=False):
        if bt:
            self.bt_time = self.bt_time + action
        else:
            self.time = self.time + action
            
    # get the time vector
    def getTimeVec(self,bt=False):
        if bt:
            return self.bt_time
        else:
            return self.time








    






