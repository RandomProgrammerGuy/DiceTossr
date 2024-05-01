import random
from matplotlib import pyplot as plt

n_at_fifth_throw = []

iterations = 1000000
x = 0 

while x <= iterations:

    dice = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,]

    n = 1

    while n <= 5:     
        for i in range(len(dice)):
            dice[i] = random.randint(1, 6)

        dice = list(filter(lambda x: x != 6, dice))

        n += 1

    n_at_fifth_throw.append(len(dice))

    x += 1

plt.subplot(facecolor = 'azure')
plt.hist(n_at_fifth_throw, facecolor = 'darkslategray', edgecolor = 'black', bins = 20)
plt.title('REMAINING DICE AFTER 5TH THROW', fontweight='bold', family='serif')
plt.xlabel('Number remaining', fontstyle='italic', family='serif')
plt.ylabel('Occurence', fontstyle='italic', family='serif')
plt.tight_layout()
plt.show()