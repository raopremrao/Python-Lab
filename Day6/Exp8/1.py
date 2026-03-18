# Sub Function
# The re.sub() function in Python stands for substitute. It is part of the re (regular expression) 
# module and is used to replace occurrences of a particular pattern in a string.

import re

string = "She sells sea shells on the sea shore"
pattern = "sea"
repl = "ocean"
new_string = re.sub(pattern, repl, string, count=1)
print(new_string)