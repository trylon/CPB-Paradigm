import robot_talk as rt
import math



class manage_world_tour(rt.Component):
    def __init__(self):
        self.positions = [[1,1][1,-1][-1,-1],[-1,-1]]
        self.current_index = 0
        self.done = False
    def execute(self):
        while not self.should_pause:
            if not self.done :
                robot_position = rt.pull_data("robot_position")
                if rt.distance(robot_position,self.positions[self.current_index]) < 0.1 : 
                    current_index += 1
                    if current_index >= len(self.positions):
                        self.done = True
                        rt.delete_type("mark")
                    else : rt.fuse(rt.create("mark",absolute_position=self.positions[self.current_index])) 
            time.sleep(1.0)
