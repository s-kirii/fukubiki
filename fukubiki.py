"""
Import area
"""
import random as rd
from time import sleep
import logging

"""
Config area
"""
DebugMode=False #If you wanna debug, change to True.
logging.basicConfig(level=logging.DEBUG) if DebugMode else logging.basicConfig(level=logging.INFO)

"""
Main codes area
"""
class box():
    def __init__(self, number_of_ball=100, win=2):
        self.NoB = number_of_ball
        self.win = win
        self.lose = self.NoB - self.win
        self.result=[]
        self.balls=[]
        for i in range(self.win):
            self.balls.append("win")
        for i in range(self.lose):
            self.balls.append("lose")
        
    def pick_ball(self,times=1, presult=True, wait=3):
        if len(self.balls)<times:
            if presult: print("玉が足りません...")
            logging.error({"error":"Not enough to take the number of balls you assigned."})
        else:
            for i in range(times):
                logging.info({"info":"Take balls..."})
                sleep(wait)
                n=rd.randint(0,len(self.balls)-1)
                r=self.balls.pop(n)
                if r=="win":
                    logging.info({"info":"Win"})
                    if presult: print("当たりです！！おめでとう！！")
                else:
                    logging.info({"info":"Lose"})
                    if presult: print("残念...はずれ...")
                self.result.append(r)
                if len(self.balls)==0:
                    logging.warning({"warning":"The balls are gone."})
                    if presult: print("玉がなくなりました")


"""
Test codes area
"""
if __name__=="__main__":
    box=box(number_of_ball=3, win=1)
    box.pick_ball(times=3, presult=False, wait=1)
    box.pick_ball()
