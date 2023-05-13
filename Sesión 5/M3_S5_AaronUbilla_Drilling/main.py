word = "paralelepipedo"

# Recorriendo una lista
vowels_list = ['a', 'e', 'i', 'o', 'u']

for i in range(len(vowels_list)):
    word = word.replace(vowels_list[i], '')

print(word)

# ---------------------------------------------------

# Recorriendo un string
vowels2 = "aeiou"

for e in vowels2:
    word = word.replace(e, "")

print(word)
