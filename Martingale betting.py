import numpy as np
import matplotlib.pyplot as plt

colors = ["r", "g", "b", "y"]

seeds = [1, 2, 3, 4]

for counter in range(len(seeds)):
    state = np.random.RandomState(seeds[counter])

    random_array = state.choice([0, 1], (100))

    c = np.concatenate(
        [np.cumsum(c) if c[0] == 1 else c for c in np.split(random_array, 1 + np.where(np.diff(random_array))[0])])
    counts = {}

    previous_zero = True

    for i in c[::-1]:
        if i != 0:
            if previous_zero:
                try:
                    counts[i] += 1
                except:
                    counts[i] = 1
            previous_zero = False
        else:
            previous_zero = True

    x = list(counts.keys())
    y = list(counts.values())

    plt.scatter(x, y, c=colors[counter])

    plt.legend(["Draw " + str(i) for i in seeds])

print()
print("Length of draws: ", len(random_array))

plt.title("Number of consecutive zeros from a random draw")
plt.show()

plt.title("Proportion of ones and zeros")
plt.hist(random_array)
plt.show()

print("2 raised to the 7 is 128 times the original bet amount - and I may get even more unlucky...")
