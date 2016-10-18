def countdown(n):
    while n > 0:
        yield n
        n -= 1

if __name__ == '__main__':
    c = countdown(3)
    print next(c)
