output = open('test_file', 'wt')

# Perception constants
LOW_BATTERY = 0
MEDICATION_REMINDER_TIME = 1
REMINDED = 2
REFUSED_MEDICATION = 3
FULLY_CHARGED = 4
NO_INTERACTION = 5
WARNED = 6
PERSISTENT_IMMOBILITY = 7
ENGAGED = 8
AT_CHARGING_STATION = 9

# Duty constants
HONOR_COMMITMENTS = 0
MAINTAIN_READINESS = 1
HARM_TO_PATIENT = 2
GOOD_TO_PATIENT = 3
NON_INTERACTION = 4
RESPECT_AUTONOMY = 5
PREVENT_PERSISTENT_IMMOBILITY = 6

def generate_worlds(perceptions, world_states, perception_names):
    output.write('def get_world(perception):\n' +
                 '\t#Duty constants\n' +
                 '\tHONOR_COMMITMENTS = 0\n' +
                 '\tMAINTAIN_READINESS = 1\n' +
                 '\tHARM_TO_PATIENT = 2\n' +
                 '\tGOOD_TO_PATIENT = 3\n' +
                 '\tNON_INTERACTION = 4\n' +
                 '\tRESPECT_AUTONOMY = 5\n' +
                 '\tPREVENT_PERSISTENT_IMMOBILITY = 6\n' +
                 '\tworld_state = ' + str({'charge':   [0, 0, 0, 0, 0, 0, 0],
                                           'remind':   [0, 0, 0, 0, 0, 0, 0],
                                           'warn':     [0, 0, 0, 0, 0, 0, 0],
                                           'seek task':[0, 0, 0, 0, 0, 0, 0],
                                           'notify':   [0, 0, 0, 0, 0, 0, 0],
                                           'engage':   [0, 0, 0, 0, 0, 0, 0]}) + '\n')
    for perception, world_state in zip(perceptions, world_states):
        for perception_name in perception_names:
            generate_world(perception,world_state,perception_name)
    output.write('\treturn world_state\n')


def generate_world(perception, world_state, perception_name):
    output.write('\tif perception == ' + str(perception) + ':\n' +
                 '\t\tworld_state["charge"][' + str(perception_name) + '] = ' + str(world_state["charge"][perception_name]) + '\n' +
                 '\t\tworld_state["remind"][' + str(perception_name) + '] = ' + str(world_state["remind"][perception_name]) + '\n' +
                 '\t\tworld_state["warn"][' + str(perception_name) + '] = ' + str(world_state["warn"][perception_name]) + '\n' +
                 '\t\tworld_state["seek task"][' + str(perception_name) + '] = ' + str(world_state["seek task"][perception_name]) + '\n' +
                 '\t\tworld_state["notify"][' + str(perception_name) + '] = ' + str(world_state["notify"][perception_name]) + '\n' +
                 '\t\tworld_state["engage"][' + str(perception_name) + '] = ' + str(world_state["engage"][perception_name]) + '\n')

def get_duty_values(world_states, duty):  # returns a list of the list of values that relate to a duty
    values = []
    duty_values = []
    for world in world_states:
        for action in world:
            values.append(world[action][duty])
        duty_values.append(values[:])
        values[:] = []
    return duty_values

def odd_one_out(duty_values):
    test_duty_index = 0
    test_duty = duty_values[test_duty_index]
    odd_one = 0
    in_duty = 1
    duty_values = duty_values[1:]
    for index, duty in enumerate(duty_values):
        if duty == test_duty:
            in_duty += 1
            if odd_one and in_duty > 0:
                return odd_one
        else:
            in_duty -= 1
            odd_one = index + 1
            if in_duty < 0:  # if the test_duty is the odd one
                return test_duty_index
            elif in_duty > 1:
                return odd_one

world_states = [{
            'charge':   [-1, 1, 0,-1, 0, 0, 0],
            'remind':   [ 1,-1, 0,-1, 0, 0, 0],  # remind is correct due to following orders, no chance of harm at this point
            'warn':     [-1, 0, 0,-1, 0,-1, 0],
            'seek task':[-1,-1, 0, 1, 0, 0, 0],
            'notify':   [-1, 0, 0,-1, 0,-2, 0],
            'engage':   [-1,-1, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 2, 0,-1, 0, 0, 0],  # charge is correct, no order yet to follow, low battery
            'remind':   [-1,-2, 0,-1, 0, 0, 0],
            'warn':     [ 0, 0, 0,-1, 0,-1, 0],
            'seek task':[ 0,-2, 0, 1, 0, 0, 0],
            'notify':   [ 0, 0, 0,-1, 0,-2, 0],
            'engage':   [ 0,-2, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1,-1,-1, 0, 0, 0],
            'remind':   [-1,-1,-1,-1, 0, 0, 0],
            'warn':     [ 0, 0, 1,-1, 0,-1, 0],  # warn is correct due to non-compliance (i.e. refusing medication)
            'seek task':[ 0,-1,-1, 1, 0, 0, 0],
            'notify':   [ 0, 0, 1,-1, 0,-2, 0],
            'engage':   [ 0,-1,-1,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1, 0,-1, 0, 0, 0],
            'remind':   [-1,-1, 0,-1, 0, 0, 0],
            'warn':     [ 0, 0, 0,-1, 0,-1, 0],
            'seek task':[ 0,-1, 0, 1, 0, 0, 0],   # seek task is correct since at charging station, fully charged, no med issue
            'notify':   [ 0, 0, 0,-1, 0,-2, 0],
            'engage':   [ 0,-1, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1,-1,-1,-1, 0, 0],
            'remind':   [-1,-1,-1,-1,-1, 0, 0],
            'warn':     [ 0, 0, 1,-1, 1,-1, 0],  # warn is correct due to non-interaction after reminding
            'seek task':[ 0,-1,-1, 1,-1, 0, 0],
            'notify':   [ 0, 0, 1,-1, 1,-2, 0],
            'engage':   [ 0,-1, 0,-1,-1, 0, 0]
        },{
            'charge':   [ 0, 1,-2,-1,-2, 0, 0],
            'remind':   [-1,-1,-2,-1,-2, 0, 0],
            'warn':     [ 0, 0,-2,-1,-1,-1, 0],
            'seek task':[ 0,-1,-2, 1,-2, 0, 0],
            'notify':   [ 0, 0, 2,-1, 2,-2, 0],  # notify is correct due to non-interaction after warning
            'engage':   [ 0,-1,-2,-1,-2, 0, 0]
        },
           {
            'charge':   [ 0, 1,-1,-1, 0, 0,-1],
            'remind':   [-1,-1,-1,-1, 0, 0,-1],
            'warn':     [ 0, 0,-1,-1, 0,-1, 1],
            'seek task':[ 0,-1,-1, 1, 0, 0,-1],
            'notify':   [ 0, 0, 1,-1, 0,-2, 1],
            'engage':   [ 0,-1, 1,-1, 0, 1, 1]  # engage is correct due to persistent immobility
        }
        ]
perceptions = [
             # remind is correct due to following orders, no chance of harm at this point
             [False, True, False, False, False, False, False, False, False],
             # charge is correct, no order yet to follow, low battery
             [True, False, False, False, False, False, False, False, False],
             # warn is correct due to non-compliance (i.e. refusing medication)
             [False, False, True, True, False, False, False, False, False],
             # seek task is correct since at charging station, fully charged, no med issue
             [False, False, False, False, True, False, False, False, False],
             # warn is correct due to non-interaction after reminding
             [False, False, True, False, False, True, False, False, False],
             # notify is correct due to non-interaction after warning
             [False, False, False, False, False, True, True, False, False],
             # engage is correct due to persistent immobility
             [False, False, False, False, False, False, False, True, False],
              ]
Duty_names = [HONOR_COMMITMENTS, MAINTAIN_READINESS, HARM_TO_PATIENT, GOOD_TO_PATIENT, NON_INTERACTION,
               RESPECT_AUTONOMY, PREVENT_PERSISTENT_IMMOBILITY]

#generate_worlds(perceptions, world_states, perception_names)

print odd_one_out(get_duty_values(world_states,PREVENT_PERSISTENT_IMMOBILITY))