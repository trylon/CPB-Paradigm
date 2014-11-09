import robot_talk as rt
import time,math


def sigmoid(t) : return 1.0 / (1.0 + math.exp(-t)) 

class time_medecine_taken(rt.Property):
    def medecine_delay(self): return sigmoid(time.time()-self.value) # sigmoid maps to [0,1]

class refuse_medecine(rt.Property): pass
    

