# Define the source string containing email metadata
info = "From raom61337@gmail.com Sun Oct 16 20:29:16 2026"

# 1. Extract the Mail Server (domain)
# Find the index of '@' and move 1 character forward to start after it
start = info.find("@") + 1
# Find the index where '.com' ends by adding its length (4) to its starting position
end = info.find(".com") + 4
# Slice the string from 'start' to 'end' to get 'gmail.com'
mailserver = info[start:end]

# 2. Extract the Date and Time
# Set the new start position to one character after the previous 'end' (skipping the space)
start = end + 1
# Set the end position to the total length of the string to capture everything until the end
end = len(info)
# Slice the string from the new 'start' to the end of the string
date_time = info[start:end]

# Output the results
print("The email has been sent through " + mailserver) 
print("It was sent on " + date_time) 