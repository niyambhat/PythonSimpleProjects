def read_file(file_name):
    ### WRITE SOLUTION HERE
    textFile = open(file_name,"r")
    fileContent=textFile.read()
    print(fileContent)
    return fileContent
    # raise NotImplementedError()

def read_file_into_list(file_name):
    file = open(file_name)
    lines=[]
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line)
    print(lines)
    return lines
    # raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    ### WRITE SOLUTION HERE
    firstLine = "Hello world"
    with open(output_filename, "w") as file :
        file.write(firstLine + '\n')  # Add a newline character to the end of the line
    # raise NotImplementedError()


def read_even_numbered_lines(file_name):
    lines = []
    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number % 2 == 0:
                lines.append(line)
    return lines

    # raise NotImplementedError()

def read_file_in_reverse(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in reversed(file.readlines()):
            lines.append(line.strip())
    return lines
    # raise NotImplementedError()

def main():
    file_contents = read_file("sampletext.txt")
    fileContentList = read_file_into_list("sampletext.txt")
    print(fileContentList)
    write_first_line_to_file(fileContentList, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()