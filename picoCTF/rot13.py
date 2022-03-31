encFlag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
decFlag = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
rotAlphabet = alphabet[13:] + alphabet[:13]

for char in encFlag:
    upper = False
    if char.isupper():
        upper = True
        char = char.lower()
    if char in alphabet:
        if upper: decFlag += rotAlphabet[alphabet.index(char)].upper()
        else: decFlag += rotAlphabet[alphabet.index(char)]
    else:
        decFlag += char

print(decFlag)