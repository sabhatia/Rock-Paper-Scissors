# CLI interface
from pickle import TRUE
from rock_paper_scissors_core import game_constants as K
from rock_paper_scissors_core import player_data
from rock_paper_scissors_core import moves as moves

# Import Key functions
from rock_paper_scissors_core import get_move_str
from rock_paper_scissors_core import evaluate_turn
from rock_paper_scissors_core import make_a_move

from pprint import pprint

user_choices = [move for move in moves]
user_choices.insert(0, "quit")

def set_total_players(players_in_game):
    assert(players_in_game <= K["MAX_PLAYERS_COUNT"])

    player_data["players"] = players_in_game    
    # Initialize the players structures
    for indx in range(0, player_data['players']):
        player_data["scores"].append(0)
        player_data["choices"].append(0)

def get_total_players():
    players_count = int(input("Enter number of players (2 - 5): "))
    if players_count < K["MIN_PLAYERS_COUNT"] or \
       players_count > K["MAX_PLAYERS_COUNT"]:
        print("Invalid count. Valid players {} - {}.".format(K["MIN_PLAYERS_COUNT"], K["MAX_PLAYERS_COUNT"]))
        return (K["INVALID_PLAYERS_COUNT"])
    return (players_count)

def is_valid_user_choice(selected_choice):
    if (selected_choice in range(0, len(user_choices))):
        return True
    
    return False

def get_user_choice():
    print("Enter a value for your turn. Choices are:")
    for choice_indx in range(0, len(user_choices)):
        print("{}: {}".format(choice_indx, user_choices[choice_indx]))
    return(int(input("Your selection: ")))

def get_valid_user_choice():
    user_choice = get_user_choice()

    while not is_valid_user_choice(user_choice):
        print("Invalid choice[{}]. Valid ranges are [{}] - [{}]".format(user_choice,
        0, len(user_choices)-1))
        user_choice = get_user_choice()
    
    return (user_choice)
    
def initialize_game():
    # 1. Find how many players there are
    while (player_data['players'] == K["INVALID_PLAYERS_COUNT"]):
        player_data['players'] = get_total_players()

    # 2. Initialize the data structures
    for indx in range(0, player_data['players']):
        player_data["scores"].append(0)
        player_data["moves"].append(0)

def play_rock_paper_scissors():
    # 1. Intialize the game
    player_scores = player_data['scores']
    player_moves = player_data['moves']
    total_players = player_data['players']

    # 2. Get the player's move
    user_choice = get_valid_user_choice()
    print("You chose [{}]".format(user_choices[user_choice]))

    # 3. Do they want to quit
    if user_choices[user_choice] == "quit":
        exit()

    # 4. Nope. Determine the user's move
    player_moves[K["USER_PLAYER_ID"]] = get_move_str(user_choice)

    #5. Generate other player choices
    for player in range(K["USER_PLAYER_ID"] + 1, total_players):
        player_moves[player] = make_a_move()
        print("Player[{}] draws {}".format(player+1, player_moves[player]))

    # 6. Evaluate the score for each player
    for player in range(0, total_players):
        for opponent in range(0, total_players):
            if evaluate_turn(player_moves[player], player_moves[opponent]) == "win":
                player_scores[player] += 1

def print_scores():

    # Print Banner
    print('=' * 80)
    print('\tGame Score'.format())
    print('=' * 80)

    # Print the player scores
    for indx in range(0, player_data['players']):
        print("\tPlayer [{}]: {}".format(indx+1, player_data['scores'][indx]))
    
    # Blank Line
    print()
