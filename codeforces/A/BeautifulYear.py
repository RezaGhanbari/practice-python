x = raw_input()
for i in range(eval(x)+1, 9013):
    if len(set(str(i))) == 4:
        print i
        break
