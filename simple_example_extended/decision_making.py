import robot_talk as rt
import time,math
from collections import Counter,deque
from robot_talk_drivers_rt import set_ethical_score


def ethical_thinking(possible_actions):
    # here code that do several things:
    # for example (but that can be anything): 
    # 1. compute the ethical values
    # 2. run geneth
    # 3. possibly does some post processing
    # return selected action, e.g. GIVE_MEDICINE


action_history = deque(10);
def resolve_action_thrashing(selected_action):
    global action_history
    action_history.append(selected_action)
    return Counter(action_history).most_common(1)[0]
    

def decision_making():

    while not rt.stopped():

        # some action might not be available. e.g. GIVE_MEDICINE if the patient left. This is updated automatically at lower level.
        possible_actions = rt.get_possible_actions() 

        # what should be the robot doing ?
        selected_action = ethical_thinking(possible_actions)

        # risk of action thrashing (robot changing its mind about what to do at each iteration). Solved below:
        selected_action = resolve_action_thrashing(selected_action)

        # give results to TDM
        scores = {action:-1 for action in possible_actions}
        scores[selected_action] = 1
        set_ethical_score(scores)

        # frequency can be configured.
        time.sleep(1)
    
