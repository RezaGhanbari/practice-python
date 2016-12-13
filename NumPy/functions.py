def sign(x):
    if x > 0:
        print 'positive'
    elif x < 0:
        print 'negative'
    elif x == 0:
        print 'Zero'


for x in range(-1, 2, 1):
    sign(x)


def hello(name, loud=False):
    if loud:
        print 'HELLO, %s' % name.upper()
    else:
        print 'Hello, %s' % name


hello('Reza')
hello('Mr. Ghanbari', loud=True)
