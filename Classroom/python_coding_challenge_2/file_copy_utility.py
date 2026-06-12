'''Problem Statement 
Sample Input/Data 
Source File (notes.txt) 
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 
Tasks 
1. Read the contents of the source file.  
2. Copy the entire content to another file named backup.txt.  
3. Display a success message.  
4. Verify whether both files contain the same number of lines.  
Sample Output 
File copied successfully. 
 
Source File Lines: 3 
 
Backup File Lines: 3 
 
Verification Status: Successful'''
# program to make File Copy Utility
# Read contents from notes.txt and copy to backup.txt

# Read source file
source = open("notes.txt", "r")
content = source.read()
source.close()

# Copy content to backup file
backup = open("backup.txt", "w")
backup.write(content)
backup.close()

print("File copied successfully.\n")

# Count lines in source file
source = open("notes.txt", "r")
source_lines = len(source.readlines())
source.close()

# Count lines in backup file
backup = open("backup.txt", "r")
backup_lines = len(backup.readlines())
backup.close()

print("Source File Lines:", source_lines)
print("Backup File Lines:", backup_lines)

# Verification
if source_lines == backup_lines:
    print("Verification Status: Successful")
else:
    print("Verification Status: Failed")