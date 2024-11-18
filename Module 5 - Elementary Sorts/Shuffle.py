from random import randrange

class StdRandom():
    def shuffle(self, l):
        for i in range(len(l)):
            random_index = randrange(0, i + 1)

            l[i], l[random_index] = l[random_index], l[i]