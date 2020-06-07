trigger_file = open("triggers.txt", 'r')
lines = []
for line in trigger_file:
    line = line.rstrip()
    if not (len(line) == 0 or line.startswith('//')):
        lines.append(line)
triggers_list = []
triggers_dict = {}
for line in lines:
    triggers_list.append(line.split(","))

for i in range(len(triggers_list)):
    if triggers_list[i][1] == "TITLE":
        triggers_dict[triggers_list[0]] = T

print(triggers_list)
