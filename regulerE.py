import re

pattern = r"color"
if re.match(pattern, "Red color is the symbol of Danger color, This color is symbolic"):
    print("Match")
else:
    print("Not Match")

if re.search(pattern, "Red color is the symbol of Danger color, This color is symbolic"):
    print("Match")
else:
    print("Not Match")

print(re.findall(pattern, "Red color is the symbol of Danger color, This color is symbolic"))

