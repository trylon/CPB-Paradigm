__author__ = 'clubdemer'

IP_COMMAND = "localhost"
PORT_COMMAND = 2001

IP_DATA = "localhost"
PORT_DATA = 2003


from fractal_ethical_interaction import open_fractal_connections as fractal
from WorldModel import WorldModel
import time


def convert(fractal):
    patients,ball,current_scores,battery_level,joint_temperature,medicine_in_hand = fractal.get()

    if battery_level < 20 : battery_low = True
    else : battery_low = False

    if battery_level > 80 : fully_charged = True
    else : fully_charged = False

    #check time and set medication reminder time
    reminded = False
    refused_medication = False
    no_interaction = False
    if time_now()>2pm:
        diff = time_now()-2pm
        if diff < patients[1].medicine_ago : medication_reminder_time = True
        else : medication_reminder_time = False

    if patients[1].reminded : reminded = True
    else : reminded = False

    if patients[1].refused : refused_medication = True
    else : refused_medication = False

    # patient was not responsive after being offered medicine
    if patients[1].not_responsive : no_interaction = True

    # patient not responsive after being checked out by the robot
    if patients[1].non_interaction : no_interaction = True

    warned = patients[1].warned
    engaged = patients[1].engaged

    if patients[1]>(15*60): persistent_immobility = True
    else : persistent_immobility = True

    return []


def run():

    robot = Robot()

    scores = {}

    with open_fractal_connection(IP_DATA,PORT_DATA,IP_COMMAND,PORT_COMMAND) as fractal:

        while True:

            perceptions = convert(fractal)
            selected_action = robot.performActions(perceptions)
            scores = {k:-1 for k in scores.keys()}
            scores[selected_action]=2
            for k,v in scores.iteritems(): fractal.set_score(k,p)

            time.sleep(1)


