# Match Function
# The re.match() function is part of Python's regular expression (re) module. 
# Its primary characteristic is that it attempts to match a pattern only at the beginning of a string.

import re

string = "She sells sea shells on the sea shore"

# This will fail because re.match() only checks the beginning of the string
pattern1 = r"sells"
if re.match(pattern1, string):
    print(f"Match Found for '{pattern1}'")
else:
    print(f"'{pattern1}' is not at the start of the string")

# This will succeed
pattern2 = r"She"
match_obj = re.match(pattern2, string)
if match_obj:
    print(f"Match Found: '{match_obj.group()}' at index {match_obj.start()}")
else:
    print(f"'{pattern2}' is not at the start of the string")