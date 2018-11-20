def check_puzzle(puzzle, size):
    if puzzle == None or size == None:
        return None
    cmpt = 0
    flat_list = []
    for sublist in puzzle:
        if len(sublist) != size:
            print("Error line lenght")
            return False
        for item in sublist:
            if (item >= size**2 or item < 0):
                print("Error item too big or < 0")
                return False
            flat_list.append(item)
        cmpt += 1
    if len(flat_list) != len(set(flat_list)) or cmpt != size:
        print("Error col size or duplicate")
        return False
    return True

def remove_comment(line):
    index = line.find('#')
    if index >= 0:
        line = line[:index]
    return line.strip()

def parse_puzzle(file_path):
    puzzle = []
    size = 0

    try:
        f = open(file_path, 'r')
    except:
        print("Cannot open file")
        return None, None

    while True:
        try:
            line = f.readline()
        except:
            return None, None
        if len(line) == 0:
            break
        line = line.rstrip()
        if not line.isprintable():
            return None, None
        line = remove_comment(line)
        if len(line) == 0 and size > 0:
            return None, None
        if len(line) > 0 and size == 0:
            if not line.isdigit():
                return None, None
            size = int(line)
            if size <= 0 or size > 10:
                return None, None
        elif size > 0:
            split = line.split(' ')
            for s in split:
                if not s.isdigit():
                    return None, None
            puzzle.append([int(s) for s in split])
    return puzzle, size
