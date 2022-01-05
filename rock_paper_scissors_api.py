# CLI interface
from rock_paper_scissors_core import game_constants as K
from rock_paper_scissors_core import player_data
from rock_paper_scissors_core import moves as moves

# Import Key functions
from rock_paper_scissors_core import get_move_str
from rock_paper_scissors_core import evaluate_turn
from rock_paper_scissors_core import make_a_choice

from pprint import pprint

def set_total_players(players_in_game):
    assert(players_in_game <= K["MAX_PLAYERS_COUNT"])

    player_data["players"] = players_in_game    
    # Initialize the players structures
    for indx in range(0, player_data['players']):
        player_data["scores"].append(0)
        player_data["choices"].append(0)

def get_total_players():
    players_count = int(input("Enter number of players(2-5): "))
    if players_count < K["MIN_PLAYERS_COUNT"] or \
       players_count > K["MAX_PLAYERS_COUNT"]:
        print("Invalid count. Valid players {} - {}.".format(K["MIN_PLAYERS_COUNT"], K["MAX_PLAYERS_COUNT"]))
        return (K["INVALID_PLAYERS_COUNT"])
    return (players_count)

def valid_user_choice(selected_choice):
    return (selected_choice >= 1 and selected_choice <= len(moves))

def get_user_choice():
    print("Enter a value for your turn. Choices are:")
    for choice_indx in range(0, len(moves)):
        print("{}: {}".format(choice_indx+1, moves[choice_indx]))
    return(int(input("Your selection: ")))

def get_valid_user_choice():
    user_choice = get_user_choice()

    while not valid_user_choice(user_choice):
        print("Invalid selection: [{}]. Valid values are [1 - {}].".format(
            user_choice, len(moves)))
        user_choice = get_user_choice()
    
    return (user_choice)
    
def initialize_game():
    # 1. Find how many players there are
    while (player_data['players'] == K["INVALID_PLAYERS_COUNT"]):
        player_data['players'] = get_total_players()

    # 2. Initialize the data structures
    for indx in range(0, player_data['players']):
        player_data["scores"].append(0)
        player_data["choices"].append(0)

def play_rock_paper_scissors():
    # 1. Play a turn - Get user choice
    player_scores = player_data['scores']
    player_choices = player_data['choices']
    total_players = player_data['players']

    player_choices[K["USER_PLAYER_ID"]] = get_move_str(get_valid_user_choice())
    print("You drew {}".format(player_choices[K["USER_PLAYER_ID"]]))

    #2. Generate other player choices
    for player in range(K["USER_PLAYER_ID"] + 1, total_players):
        player_choices[player] = make_a_choice()
        print("Player[{}] draws {}".format(player+1, player_choices[player]))

    # 3. Evaluate the score for each player
    for player in range(0, total_players):
        for opponent in range(0, total_players):
            if evaluate_turn(player_choices[player], player_choices[opponent]) == "win":
                player_scores[player] += 1

def print_scores():
    for indx in range(0, player_data['players']):
        print("Player[{}]: {}".format(indx+1, player_data['scores'][indx]))

def play_user_turn():
    return

def play_comp_turn():
    return