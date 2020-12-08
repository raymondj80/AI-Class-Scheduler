from Class import Class
import numpy as np

class TimeSlot:
    def __init__(self,time):
        self.time = time
        self.max_action = None
        self.max_class = None
        self.work_done = False
        self.utility = 0

    #Returns all the valid actions available for a particular time
    def get_valid_actions(self,classList):
        Actions = []
        for Class in classList:
            if self.time in Class.class_times:
                Actions.append([Class,np.array([1,0,0])])
            if self.time in Class.oh_times:
                Actions.append([Class,np.array([0,1,0])])
            # Work is always a valid option
            Actions.append([Class,np.array([0,0,1])])
        return Actions

    #Calculates the maximum utility of the timeslot
    def calc_utility(self,valid_Actions,bt=False):
        V = None
        work_done = False
        for action in valid_Actions:
            done = False
            Class, t_action = action

            D = Class.difficulty
            t_prev = Class.getTimeVec(bt)
            t_curr = t_prev + t_action


            W_curr = min(self.E_Pset(t_prev,D),self.W_Pset(t_curr))
            E_curr = max(self.E_Pset(t_curr,D),W_curr)

            # calculates the change in Expected Pset Hours 
            del_E = self.E_Pset(t_prev,D) - E_curr

            # calculates the change in Amount of Work Done
            del_W = W_curr - self.W_Pset(t_prev)

            # Utility Calculation
            Q = Class.weight * np.exp(-np.abs((Class.deadline-self.time)/168)) * (del_E + del_W)

            # Determine if work is done
            if abs(W_curr - E_curr) < 0.001:
                done = True

            if V is None or Q > V:
                work_done = done
                C_max = Class
                V = Q
                a_max = t_action

        if bt:
            self.max_class = C_max
            self.max_action = a_max
            
        self.utility = V
        self.work_done = work_done
        return a_max

    # Calculates the Expected Pset Time
    def E_Pset(self,time,difficulty):
        return difficulty * np.exp(-1.3 * time[0]/4) * np.exp(-0.9 * time[1]/4) + difficulty
    
    # Calculates the Work Done 
    def W_Pset(self,time):
        return (1 + 0.2 * np.sqrt(time[0]/10) + 0.5 * np.sqrt(time[1]/5)) * time[2]



    

    
