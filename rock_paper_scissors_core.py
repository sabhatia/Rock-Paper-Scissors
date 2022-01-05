from pprint import pprint
from random import seed
from random import choice
import time

moves = ["rock", "paper", "scissors"]
result = ["win","lose"]

rules = {"rock": ["scissors"], 
        "scissors": ["paper"], 
        "paper": ["rock"]}

game_constants = {
    "INVALID_PLAYERS_COUNT": -1,
    "INVALID_USER_CHOICE": -1,
    "CHOICE_QUIT": 0,

    "MIN_PLAYERS_COUNT": 2,
    "MAX_PLAYERS_COUNT":5,
    "USER_PLAYER_ID": 0,
}

player_data = {'scores':[], 'choices':[], 'players': game_constants['INVALID_PLAYERS_COUNT']}

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
