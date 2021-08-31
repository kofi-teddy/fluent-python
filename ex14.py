# Opening a file

stream = open(file_name, mode, buffer_size)

"""
Modes
r - Reads (default)
w - Truncate
a - Append
x - Write
+ - Updating (read/write)

t - Text(defualt)
b - Binary
"""


stream = open("demo.txt")

# Check if readable 
print(stream.readable())

# Read first character
print(stream.read(1))

# Read fist line
print(stream.readline())

# Close the stream
stream.close()


stream = open("output.txt", "wt")
stream.write("H")
stream.writeline(["ello", " ", "world"])
stream.write("\n")
names = ["Priscilla", "Baaba"]
stream.writeline(names)

stream.close()


stream = open("output.txt", "wt")
stream.write("demo")
stream.seek(0) # Put the cursor back at the start
stream.write("cool")
stream.flush() # Write the data to file
stream.close() # Flush and close the stream 
