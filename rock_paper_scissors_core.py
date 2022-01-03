from pprint import pprint
from random import seed
from random import choice
import time

moves = ["rock", "paper", "scissors"]
result = ["win","lose"]

rules = {"rock": ["scissors"], 
        "scissors": ["paper"], 
        "paper": ["rock"]}

seed(time.time())


def get_move_str(move_id):
    if (move_id < 1 or move_id > len(moves)):
        return ("Invalid Id {}. Range [1 - {}])".format(move_id, len(moves)))
    
    # Valid Id: Look into the list for the correct string
    return (moves[move_id - 1])

def make_a_choice():
    # get a choice from the list of possible moves
    return(choice(moves))
   
def evaluate_turn(choiceA, choiceB):
    assert(choiceA in moves)
    assert(choiceB in moves)

    # If both are same, it's a draw
    if choiceB == choiceA:
        return "draw"

    if choiceB in rules[choiceA]:
        return "win"
    else:
        return "lose"
