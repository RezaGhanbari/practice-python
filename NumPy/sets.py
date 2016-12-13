animals = {'cat', 'dog', 'spider', 'lion', 'teddy', 'hen'}
for idx, animal in enumerate(animals):
    print '#%d: %s ' % (idx, animal)

# Set comprehensions
from math import sqrt
nums = {int(sqrt(x)) for x in range(40)}
print nums