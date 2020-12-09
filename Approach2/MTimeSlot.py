from MarkovClass import MarkovClass
import numpy as np

class MTimeSlot:
    """
    Timeslot class that represents a 1 hour timeslot in the work schedule
    
    Atrtributes
    -----------
    time: int
        time of TimeSlot class
    max_action: np.array
        best action chosen by calc_utility
    max_class: Class object
        Class of max_action
    work_done: int
        percent of work done
    utility: float
        max utility calculated by calc_utility
    fatigue: int
        fatigue level
    proficiency: int
        proficiency level
    """

    def __init__(self,time):
        self.time = time
        self.max_action = None
        self.max_class = None
        self.work_done = 0
        self.utility = 0
        self.fatigue = 0
        self.proficiency = 0


    def get_valid_actions(self,classList):
        "Returns the possbile actions at the timeslot time"
        Actions = []
        for Class in classList:
            if Class.state[2] != 100:
                if self.time in Class.class_times:
                    Actions.append([Class,'class'])
                if self.time in Class.oh_times:
                    Actions.append([Class,'oh'])
            # Work and rest are always valid options
                Actions.append([Class,'work'])
            Actions.append([Class,'rest'])
        return Actions

    def calc_utility(self,valid_Actions):
        "Calculates the maximum utility of the timeslot"
        V = None
        for a in valid_Actions:
            done = False
            Class, action = a

            #Utility Calculation
            Q = Class.weight * (Class.R(Class.state,action) + np.abs((Class.deadline-self.time)/168) * Class.Q[Class.T(Class.state,action)])   

            if Class.T(Class.state,action)[2] == 100:
                done = True        

            # Determine if work is done
            if V is None or Q > V:
                work_done = done
                C_max = Class
                V = Q
                a_max = action
     
        self.max_class = C_max
        self.max_action = a_max
        self.utility = V
        self.fatigue = self.max_class.T(self.max_class.state,self.max_action)[0]
        self.proficiency = self.max_class.T(self.max_class.state,self.max_action)[1]/(self.max_class.difficulty * 10)
        self.work_done = self.max_class.T(self.max_class.state,self.max_action)[2]

    def updateState(self,classList):
        "Updates the fatigue level of all Class.state in classList"
        for Class in classList:
            if Class == self.max_class:
                Class.state = Class.T(Class.state,self.max_action)
            else:
                state = Class.state
                Class.state = (self.fatigue, state[1], state[2])





    

    
