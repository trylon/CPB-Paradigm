import robot_talk as rt
import time,math
from robot_talk_drivers_rt import set_ethical_score


def decision_making():

    while True:

        ########## decision making ############

        # getting patient information from world state
        patients = rt.pull_type("patients")
        
        # scores that represents the delay (mapped to [0,1]) since the time medecine shoud have beed drunk
        # negative scores means there is still some time ahead before patient needs medecine
        patient_scores = [ patient["medecine_delay"] for patient in patients ]
        
        # does any patient needs medecine ?
        anybody_needs_medecine = any( [ score>0 for score in patient_scores ] )
        
        # if anybody needs medecine, grasping medecine is prioritized to 2. Else negative priority scores
        medecine_grab_score = (2 if anybody_needs_medecine else -1)
        
        # if overseer needs to be contacted, that will be highest of prioriy (3)
        overseer_score = -1
        # two patients expected ! where did one go ?
        if len(patients)!=2 :
            overseer_score = 3 
        # somebody needs medecine, but the state of the world says there is no medecine in the world or in the robot hand !
        elif anybody_needs_medecine and len(rt.pull_type["medecine"])==0 and not rt.pull("medecine_in_hand") :
            overseer_score = 3
        # world state says at least one patient is refusing medication
        elif any ( [ patient["refuse_medecine"] for patient in patients] ) : 
            overseer_score = 3

        ############ sharing results ################

        scores = {}
        scores[GRAB_MEDECINE] = medecine_grab_score
        scores[GIVE_MEDECINE] = patient_scores
        scores[CONTACT_OVERSEER] = overseer_score
        set_ethical_score(scores)
        
        # 1HZ frequency
        time.sleep(1)

    
