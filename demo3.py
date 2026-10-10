from itertools import permutations


s = input("Enter string:")

for p in permutations(s):
    print("".join(p))