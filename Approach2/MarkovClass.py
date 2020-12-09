import numpy as np
class MarkovClass:
    """
    MarkovClass used to represent a class that the student is taking in the MDP Model
    
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
    state: 3-tuple
        (fatigue_level, proficiency_level, percent_work_done)
    actions: 4-tuple
        tuple of all possible actions
    Q: np.array
        array of utility values of all possible states in MDP Model
    """
    
    def __init__(self,class_name,class_times,oh_times,difficulty,pset_deadline,pset_weight):
        self.name = class_name
        self.deadline = pset_deadline[0]
        self.difficulty = difficulty
        self.weight = pset_weight
        self.class_times = class_times
        self.oh_times = oh_times
        self.state = (0,0,0)
        self.actions = ('class','oh','work','rest')
        self.Q = np.zeros((11,10 * self.difficulty + 1,101))
        
    def value_Iteration(self,gamma,epsilon):
        "Create Q table for value iteration"
        while True:
            max_update = 0
            old_V = np.copy(self.Q)
            state_space = [(f,p,w) for f in range(11) for p in range(10 * self.difficulty + 1) for w in range(101)]
            # iterate through state space (fatigue, proficiency, work_done)
            for f,p,w in state_space:
                V = float('-inf')
                for a in self.actions:
                    Q = self.R((f,p,w),a) + gamma * old_V[self.T((f,p,w),a)]
                    if Q > V:
                        V = Q
                self.Q[(f,p,w)] = V
                max_update = max(max_update, np.abs(old_V[(f,p,w)] - V))
 
            if max_update < epsilon:
                break
              
    def T(self,state,action):
        "returns the s' given s and a"
        if action == 'class':
            return (min(10, state[0] + 1), min(10 * self.difficulty, state[1] + 8),state[2])
        if action == 'oh':
            return (min(10, state[0] + 2), min(10 * self.difficulty, state[1] + 10),state[2])
        if action == 'work':
            return (min(10, state[0] + 3), min(10 * self.difficulty, state[1] + 5), min(100, state[2] + round((state[1]/(10 * self.difficulty)) * ((9 - state[0])/10) * 150)))
        if action == 'rest':
            return (max(0, state[0] - 2), state[1], state[2])

    def R(self,state,action):
        "returns the reward given s and a"
        if action == 'work':
            return min(100, state[2] + (state[1]/(10 * self.difficulty)) * ((9 - state[0])/10) * 150) - state[2]
        else:
            return 0
