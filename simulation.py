from collections import namedtuple
import 



# defining the schemes to be contained in memory

class patient(object):
    def __init__(self):
        self.position = "far"
        self.time_created = 0
        self.last_time_motion = 0
        self.time_asked_for_help = None
        self.last_time_drunk_drug = -2
        self.has_remote = False

class remote(object):
    def __init__(self):
        self.position = "far"
        self.time_created = 0
        
class drug(object):
    def __init__(self):
        self.position = "far"
        self.time_created = 0

# defining the memory as containers for schemes and other memory keys

class memory(object):
    def __init__(self):
        self.patients = [patient(),patient()]
        self.battery_level = 100
        self.temperature_joint = 0
        self.remote = remote()
        self.drug = drug() 
        self.current_time = 0
        self.time_last_spin = 0
        self.charging = False
    def set_everything_far(self):
        for patient in self.patients : patient.position = "far"
        if self.remote : self.remote.position = "far"
        if self.drug : self.drug.position = "far"
    def spin(self):
        time_passed = self.current_time - self.time_last_spin
        # battery level decreases
        if not self.charging : self.battery_level -= time_passed / 60.0
        else : self.charging = Falses
        # joint temperature increase
        self.temperature_joint += time_passed / 100.0
        # 5% chance for a patient to ask for help
        for patient in self.patients:
            if random.random() < 0.05 : patient.time_asked_for_help = self.current_time

# list of possible actions and effect to the memory

def bring_remote_to_patient_1(memory):
    # remote transfered from world to patient 1
    memory.remote = None 
    memory.patients[0].has_remote = True
    # robot walked away from everything except patient 1
    memory.set_everything_far()
    memory.patients[0].position = "close"
    # in takes 10sec in average to bring remote to patient
    memory.current_time += 10

def charging(memory):
    # robot walked away from everything to charge
    memory.set_everything_far()
    # robot docked to charger
    memory.charging = True
    # takes one minute per percent to recharge
    memory.current_time = (100-memory.battery_level)*60
    # robot is charged
    memory.battery_level = 100

# function for filtering action that can not be performed

def filter_actions(memory,actions):
    # cloning list to not mess with it
    possible_actions = [action for action in actions]
    # if no remote, can not bring to patients
    if not memory.remote : possible_actions.remove(bring_remote_to_patient_1)
    return possible_actions

# decision making loop

def test_ethical_decision_making():

    memory_ = memory()
    actions = [bring_remote_to_patient_1,charging]

    while memory_.battery_level > 0 and memory_.temperature_joint < 70 : # doing things until no battery or overheat
        possible_actions = filter_actions(memory_,actions) # removing some work to the ethical engine by removing actions that can not be possibly performed
        action = ethical_engine(memory_,possible_actions) # here the magic of the ethical decision making. Returns the member of possible_actions to execute
        action() # performing the selected action
        memory_.spin() # having the world going round






