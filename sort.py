
# get filename from user's input
fname = input("Enter the filename of the .txt file you want to sort (exclude the .txt extension): ")

# open the file and create an array of the lines of text
with open(f"{fname}.txt", 'r') as content:
    lines = content.readlines()

    # strip new lines and white space
    for line_idx in range(len(lines)):
        lines[line_idx] = lines[line_idx].strip()

    rtn_list = sorted(lines)

# ouput to new .txt file to copy and paste
with open('output.txt', 'w') as output:
    for line in rtn_list:
        output.write(line)
        output.write("\n")
