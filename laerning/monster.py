class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")


# create some real monsters

takjin = Monster("Black", 5)
tobakjin = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

print('I have ' + str(takjin.heads) + ' heads and I\'m ' + takjin.color)
print('I also have ' + str(tobakjin.heads) + ' heads and I\'m ' + tobakjin.color)
print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)
