def read_large_file(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


def process_file(path):
    try:
        with open(path) as file_handler:
            for line in read_large_file(file_handler):
                print line
    except:
        print 'Error Opening/Processing file'
