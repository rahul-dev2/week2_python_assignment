# Step 1  Create file 
file = open("data.txt", "w")
# step 2 writing at least five lines in the txt files
file.write("this assignment is for week 2 \n")
file.write("File handling is very important in python.\n")
file.write("we are writing this file in writing mode and then we are reading this file \n")
file.write("there are some another mode also like reading append w+ r+ a+\n")
file.write("This is the fifth line in the file.\n")

file.close()


# Step 3: Open file again to read
file = open("data.txt", "r")

content = file.read()

# Step 4: Display contents
print(content)

file.close()
