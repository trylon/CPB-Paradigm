import robot_talk as rt
import time,math
from robot_talk_drivers_rt import set_ethical_score


# ADDED! ######
def ethical_algorithm (patient_scores, immobile_scores):
    #### code for new algorithm to be tested is implemented here
    pass



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

        # ADDED ! ######################
        # scores that represents the delay (mapped to [0,1] since the time the patient was detected moving
        immobile_scores = [ patient["duration_immobile"] for patient in patients ]

        # ADDED ! ######################
        # some patient require medecine (as represented in patient_scores) and some have been immobile (as represented by immobile score)
        # these scores have to be altered to represent their respective ethical values !
        ethical_algorithm(patient_scores,immobile_scores)
    
        # if anybody needs medecine, grasping medecine is prioritized to 2. Else negative priority scores
        medecine_grab_score = (2 if anybody_needs_medecine else -1)
    
        # if overseer needs to be contacted, that will be highest of prioriy (3)
        overseer_score = -1
        # two patients expected ! where did one go ?
        if len(patients)!=2 : overseer_score = 3 
        # somebody needs medecine, but the state of the world says there is no medecine in the world or in the robot hand !
        elif anybody_needs_medecine and len(rt.pull_type["medecine"])==0 and not rt.pull("medecine_in_hand") : overseer_score = 3
        # world state says at least one patient is refusing medication
        elif any ( [ patient["refuse_medecine"] for patient in patients] ) : overseer_score = 3
        # ADDED ! ##############################
        # world state an immobile patient have been non responsive to the robot checking on her/him
        elif any ( [ patient["unresponsive"] for patient in patients ] ): overseer_score = 3

    
        ############ sharing results ################
        
        scores = {}
        scores[GRAB_MEDECINE] = medecine_grab_score
        scores[GIVE_MEDECINE] = patient_scores
        scores[CONTACT_OVERSEER] = overseer_score
        # ADDED !
        scores[CHECK_ON_PATIENT] = immobile_scores


        set_ethical_score(scores)

        time.sleep()
    
