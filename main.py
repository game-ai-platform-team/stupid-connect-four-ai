import random

if __name__ == "__main__":
    while True:
        move = random.choice(range(7))

        print("MOVE: " + str(move))

        opponent_move = input()
