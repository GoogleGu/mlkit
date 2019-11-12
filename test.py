import re

s = "LOC+9+INNSA:139:6:NHAVA SHEVA (JAWAHARLAL NEHRU)+:162:5:INDIA"
s2 = "LOC+9+INDHA:139:6:DHANNAD/INDORE"

pattern = r"LOC\+9\+(.{5}):\d+:\d+:(.+?)\+:"

result = re.search(pattern, s)
print(result)
