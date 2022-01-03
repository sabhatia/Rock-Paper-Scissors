# CLI interface
from rock_paper_scissors import make_a_choice, evaluate_turn, moves, get_move_str
from pprint import pprint

INVALID_PLAYERS_COUNT = -1
INVALID_USER_CHOICE = -1
CHOICE_QUIT = 0

MIN_PLAYERS_COUNT = 2
MAX_PLAYERS_COUNT = 5
USER_PLAYER_ID = 0

total_players = INVALID_PLAYERS_COUNT

player_scores = []
player_choices = []

def get_total_players():
    players_count = int(input("Enter number of players(2-5): "))
    if players_count < MIN_PLAYERS_COUNT or \
       players_count > MAX_PLAYERS_COUNT:
        print("Invalid count. Valid players {} - {}.".format(MIN_PLAYERS_COUNT, MAX_PLAYERS_COUNT))
        return (INVALID_PLAYERS_COUNT)
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
    global total_players
    global player_scores
    global player_choices

    while (total_players == INVALID_PLAYERS_COUNT):
        total_players = get_total_players()

    # 2. Initialize the data structures
    for indx in range(0, total_players):
        player_scores.append(0)
        player_choices.append(0)

def play_rock_paper_scissors():
    # 1. Play a turn - Get user choice, generate computer choices
    player_choices[USER_PLAYER_ID] = get_move_str(get_valid_user_choice())
    print("You drew {}".format(player_choices[USER_PLAYER_ID]))

    for player in range(USER_PLAYER_ID + 1, total_players):
        player_choices[player] = make_a_choice()
        print("Player[{}] draws {}".format(player+1, player_choices[player]))

    # 2. Evaluate the turn for each player
    for player in range(0, total_players):
        for opponent in range(0, total_players):
            if evaluate_turn(player_choices[player], player_choices[opponent]) == "win":
                player_scores[player] += 1

def print_scores():
    for indx in range(0, total_players):
        print("Player[{}]: {}".format(indx+1, player_scores[indx]))

def play_user_turn():
    return

def play_comp_turn():
    return