fp = open("text.txt", "r") #r is by default, so not really needed
print(fp.read()) #print the entire content of the file
fp.close() #good practice to close the file

#Different form to create the file
with open("text.txt","r") as fp:
    print(fp.read())

# Read from the same fil, line by line
print("Read the file line by line")
line_number = 1
with open("text.txt","r") as fp:
    for line in fp: #We iterate over the file line by line
        print(f"{line_number}:{line}",end="")
        #print(line,end="") #ask print not to add a new line
        line_number += 1
print("done printing")




