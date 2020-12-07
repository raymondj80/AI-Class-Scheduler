# AI-Class-Scheduler
Class scheduler that chooses optimal optional using a CSP &amp; MDP model


# Iteration 2
Changes
Replace CSP break time constraint with a fatigue state
  -> len(4) state vector (t_class, t_oh, t_work, fatigue)
  -> len(4) action vec <a_class, a_oh, a_work, a_rest>
  -> init fatigue = 0 
  taking action a_class, a_oh, a_work does the following:
    fatigue = min(1, fatigue + np.ln(fatigue + 1.1) * (0.2 * t_class + 0.3 * t_work + 0.5 * t_work))
  -> taking action a_rest does the following:
    fatigue = max(0, fatigue - np.ln(fatigue + 1))
      
      
