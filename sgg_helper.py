import os
import json
from collections import defaultdict

input_path = "C:\\Users\\Skyler\\Documents\\Paradox Interactive\\Stellaris\\mod\\w40ktdi\\input.txt"
output_path = "C:\\Users\\Skyler\\Documents\\Paradox Interactive\\Stellaris\\mod\\w40ktdi\\output.txt"
output_list = []


while not os.path.isfile(input_path):
    input_path = input("No input file found at "+input_path+"\nPlease enter input file path\n")

f = open(os.fsdecode(input_path))
print("Reading from "+input_path+"...")
lines = f.readlines()
f.close()

mode = input("Enter mode: 1. Reorder system ids; 2. Adjust system coords from 3x to 5x;\n3. Adjust system coords from 5x to 3x\n")
while mode is not "1" and mode is not "2" and mode is not "3":
    mode = input("Invalid input, enter 1, 2, or 3\n")

if mode is "1":
    print("Reordering system ids.")
if mode is "2":
    print("Adjusting system coords to 5x.")
    scale_factor = 1.667
if mode is "3":
    print("Adjusting system coords to 3x.")
    scale_factor = 0.6


system_id = 0
for i, line in enumerate(lines):
    if line.strip() == "":
        continue

    line_elems = line.strip().split()

    print_str = str(i+1)+". "
    for j in range(len(line_elems)):
        if line_elems[j] == "name":
            print_str = print_str+line_elems[j+2]
            count = 0
            while line_elems[j+2+count][-1] is not "\"":
                count = count+1
                print_str = print_str+" "+line_elems[j+2+count]
        if mode is "1":
            if line_elems[j] == "id":    
                system_str = " old id: "+line_elems[j+2]+"; "
                system_id = system_id + 1
                line_elems[j+2] = "\""+str(system_id)+"\""
                system_str = system_str+" new id: "+line_elems[j+2]
        if mode is "2" or mode is "3":
            if line_elems[j] == "x":
                old_x = line_elems[j+2]
                line_elems[j+2] = str(round(int(line_elems[j+2])*scale_factor))
                new_x = line_elems[j+2]
            if line_elems[j] == "y":
                old_y = line_elems[j+2]
                line_elems[j+2] = str(round(int(line_elems[j+2])*scale_factor))
                new_y = line_elems[j+2]
    if mode is "1":
        print_str = print_str+system_str
    if mode is "2" or mode is "3":
        print_str = print_str+" old position: "+old_x+", "+old_y+"; new position: "+new_x+", "+new_y
    print(print_str)

    output_list.append(" ".join(line_elems))

output_str = "\n".join(output_list)

f = open(output_path,"w")
print("Outputting to "+output_path+"...")
f.write(output_str)
f.close()
print("Done.")