import random

if __name__ == "__main__":
    count = {i: 0 for i in range(7)}

    while True:
        read = input().split(":")
        print(f"Read input: {read}")
        tag = read[0]
        data = read[1]
        print(f"Columns: {count}")
        if tag == "PLAY":
            print("finding move...")
            while True:
                num = random.randint(0, 6)
                if count[num] < 6:
                    print(f"MOVE:{num}")

                    count[num] += 1
                    break
                else:
                    print(f"Random result was {num}, but there was no space!")
        elif tag == "MOVE":
            op_move = read[1]
            count[int(op_move)] += 1
        elif tag == "BOARD":
            count = {i: 0 for i in range(7)}
            if len(data) > 0:
                for i in data.split(","):
                    count[int(i)] += 1
            print(f"Board set to: {count}")
        elif tag == "RESET":
            count = {i: 0 for i in range(7)}
