from rock_paper_scissors_core import *

turn1 = ("rock", "paper")
turn2 = ("rock", "scissors")

def test_win_loss():
    print(win_loss("rock", "paper"))
    print(win_loss("rock", "scissors"))
    
def test_draw_turn():
    player_draw = make_a_choice()
    print("Player 1:{}, Player 2:{}".format(player_draw[0], player_draw[1]))
    return player_draw

def test_play_turn():
    playerA, playerB = test_draw_turn()
    playerA_status = win_loss(playerA, playerB)

    if (playerA_status == "draw"):
        print("The turn is a draw.")
    elif (playerA_status == "win"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == "__main__":
    test_win_loss()
    test_draw_turn()
    test_play_turn()


