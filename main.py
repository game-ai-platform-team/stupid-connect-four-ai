from connect_four_lib.connect_four_engine import ConnectFourEngine
from connect_four_lib.connect_four_judge import ConnectFourJudge
from connect_four_lib.game_state import GameState

if __name__ == "__main__":
    judge = ConnectFourJudge()
    engine = ConnectFourEngine(judge=judge)

    game = ConnectFourEngine()

    while judge.is_game_over() == GameState.CONTINUE:
        try:
            opponent_move = input()

            if opponent_move != "":
                engine.add_move(opponent_move)

            move = engine.get_random_move()
            engine.add_move(move)

            print("MOVE: " + str(move))

        except ValueError:
            print("Invalid input. Please enter a valid column number.")
