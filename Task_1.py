def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            line_number = 1
            line = file.readline()
            while line:
                print(f"Line {line_number}: {line.strip()}")
                line = file.readline()
                line_number += 1
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")

read_file('sample.txt')