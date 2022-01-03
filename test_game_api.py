from rock_paper_scissors_core import get_move_str
import rock_paper_scissors_api

def test_get_total_players():
    total_players = rock_paper_scissors_api.get_total_players()
    print("Total Game Players: ", total_players)

def test_get_valid_user_choice():
    user_choice = rock_paper_scissors_api.get_valid_user_choice()
    print("User Choice: {} - {}".format(user_choice, get_move_str(user_choice)))

if __name__ == "__main__":
    #test playing thee game
    print("Initializing game...")
    rock_paper_scissors_api.initialize_game()
    turn_id = 1
    while True: 
        print("Playing turn ", turn_id)
        rock_paper_scissors_api.play_rock_paper_scissors()
        print("Current Score")
        rock_paper_scissors_api.print_scores()
        turn_id += 1
