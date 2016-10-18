def receiver():
    while True:
        item = yield
        print 'Got', item

if __name__ == '__main__':
    recv = receiver()
    next(recv)
    recv.send('Re')
    recv.send('Za')