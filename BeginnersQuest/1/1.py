constant = 0xCafe

p = [0] * 12

p[0] = chr(52037 - constant)
p[6] = chr(52081 - constant)
p[5] = chr(52063 - constant)
p[1] = chr(52077 - constant)
p[9] = chr(52077 - constant)
p[10] = chr(52080 - constant)
p[4] = chr(52046 - constant)
p[3] = chr(52066 - constant)
p[8] = chr(52085 - constant)
p[7] = chr(52081 - constant)
p[2] = chr(52077 - constant)
p[11] = chr(52066 - constant)

print("".join(p))