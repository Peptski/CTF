with open("lustighare.txt", "r") as f:
    for line in f.readlines():
        for char in line:
            print(chr(ord(char) + 3), end="")