from MarkovClass import MarkovClass
import numpy as np

class MTimeSlot:
    def __init__(self,time):
        self.time = time
        self.max_action = None
        self.max_class = None
        self.work_done = None
        self.utility = 0

    # Returns the valid actions available at self.time
    def get_valid_actions(self,classList):
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

    # Calculates the maximum utility of the timeslot
    def calc_utility(self,valid_Actions):
        V = None
        for a in valid_Actions:
            done = False
            Class, action = a

            # Utility Calculation
            Q = Class.weight * (Class.R(Class.state,action) + np.abs((Class.deadline-self.time)/168) * Class.Q[Class.T(Class.state,action)])

            if Class.T(Class.state,action)[2] == 100:
                done = True

            # Determine if work is done
            if V is None or Q > V:
                work_done = done
                C_max = Class
                V = Q
                a_max = action
     
        # Set the max class, max action, utility, etc.
        self.max_class = C_max
        self.max_action = a_max
        self.utility = V
        self.fatigue = self.max_class.T(self.max_class.state,self.max_action)[0]
        self.proficiency = self.max_class.T(self.max_class.state,self.max_action)[1]/(self.max_class.difficulty * 10)
        self.work_done = self.max_class.T(self.max_class.state,self.max_action)[2]

    #Update the Markov States for all classes
    def updateState(self,classList):
        for Class in classList:
            if Class == self.max_class:
                Class.state = Class.T(Class.state,self.max_action)
            else:
                state = Class.state
                Class.state = (self.fatigue, state[1], state[2])
