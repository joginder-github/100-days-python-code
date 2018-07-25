import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))


random.shuffle(deck)

print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

# output:
# 
# You got:
# 7 of Spade
# 4 of Heart
# 2 of Club
# 8 of Spade
# 12 of Club   