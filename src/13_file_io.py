"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'foo.txt')) as f:
    read_data = f.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

line1 = "This is a test to see if this works."
line2 = "Maybe it does or it doesn't"
line3 = "We'll have to see"

with open(os.path.join(__location__, 'bar.txt'), "w") as file:
    file.write(f"{line1}\n{line2}\n{line3}\n")

with open(os.path.join(__location__, 'bar.txt')) as f:
    read_data = f.read()
    print(read_data)