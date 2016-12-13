d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, leg in d.iteritems():
    print 'A %s has %d legs' % (animal, leg)
# Dictionary comprehensions
nums = range(5)
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_square
