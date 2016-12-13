class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if loud:
            print 'HELLO %s' % self.name.upper()
        else:
            print 'Hello %s' % self.name

g = Greeter('Reza')
g.greet()
g.greet(loud=True)