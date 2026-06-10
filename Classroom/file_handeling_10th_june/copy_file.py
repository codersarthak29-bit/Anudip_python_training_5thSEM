''' Write a program to copy entire content from one file into another'''
# Program to copy entire content from one file into another

# Open source file in read mode
source = open("text.txt", "r")

# Read all content
data = source.readlines()

# Open destination file in write mode
destination = open("copy.txt", "w")

# Write content into destination file
destination.writelines(data)

# Close both files
source.close()
destination.close()

print("File copied successfully.")
