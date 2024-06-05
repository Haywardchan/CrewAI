def format_txtoutput():
    with open('output.txt', 'r') as file:
        lines = file.readlines()

    with open('output.txt', 'w') as file:
        for line in lines:
            if not line.startswith('['):
                file.write(line)