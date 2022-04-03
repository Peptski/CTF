message = "<?php win(); ?>"
encrypted = "☻I§♀M[RBZP"
key = "beneri"
new = []

for i, c in enumerate(message):
    newVal = ord(c) ^ ord(key[i % 6])
    print("bitwise xor between {0} and {1}: {2} or {3}".format(c, key[i % 6], newVal, chr(newVal)))
    new.append(chr(ord(c) ^ ord(key[i % 6])))

with open("sneaky.php", "w") as f:
    for c in new:
        f.write(c)