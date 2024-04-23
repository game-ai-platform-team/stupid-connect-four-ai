if __name__ == "__main__":
    count = [0] * 7

    while True:
        read = input().split(":")
        print(f"Read input: {read}")
        tag = read[0]
        data = read[1]
        print(f"Columns: {count}")

        if tag == "PLAY":
            print("finding move...")

            for i, value in enumerate(count):
                if value < 6:
                    print(f"MOVE:{i}")
                    count[i] += 1
                    break

            print("MOVE: -1")
            print("Error: No moves left!")

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
