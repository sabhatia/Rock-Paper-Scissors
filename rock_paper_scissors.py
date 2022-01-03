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

def win_loss(drawA, drawB):
    assert(drawA in moves)
    assert(drawB in moves)

    # If both are same, it's a draw
    if drawB == drawA:
        return "draw"

    if drawB in rules[drawA]:
        return "win"
    else:
        return "lose"

def make_a_choice():
    # get a choice from the list of possible moves
    return(choice(moves))
   
def evaluate_turn(playerA, playerB):
    return win_loss(playerA, playerB)

