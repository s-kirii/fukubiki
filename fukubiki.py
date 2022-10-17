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
    def __init__(self, number_of_balls=100, win=2):
        self.NoB = number_of_balls
        self.win = win
        self.lose = self.NoB - self.win
        self.result=[]
        self.balls=[]
        for i in range(self.win):
            self.balls.append("win")
        for i in range(self.lose):
            self.balls.append("lose")
        
    def pick_ball(self,times=1, presult=False, wait=3):
        if len(self.balls)<times:
            if presult: print("Balls are not enough...")
            logging.error({"error":"Not enough to take the number of balls you assigned."})
        else:
            for i in range(times):
                logging.info({"info":"Take balls..."})
                sleep(wait)
                n=rd.randint(0,len(self.balls)-1)
                r=self.balls.pop(n)
                if r=="win":
                    logging.info({"info":"Win"})
                    if presult: print("You win! Congratulations!")
                else:
                    logging.info({"info":"Lose"})
                    if presult: print("You lose...Sorry...")
                self.result.append(r)
                if len(self.balls)==0:
                    logging.warning({"warning":"All balls are gone."})
                    if presult: print("All balls are gone.")


"""
Test codes area
"""
if __name__=="__main__":
    test=box(number_of_balls=3, win=1)
    test.pick_ball(times=3, presult=True, wait=1)
    test.pick_ball()
