
# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on 

# filenames of arbitrary length? - filename contain any  number of character

filename = "README.txt"

# str.rfind() find the position of the last dot

# Find the position of the dot in the filename
dot_position = filename.rfind('.')

# Get the extension
extension = filename[dot_position+1:]
print("Extension: ", extension)

# Get the filename without the extension
filename_without_extension = filename[:dot_position]
print("Filename without extension: ", filename_without_extension)
