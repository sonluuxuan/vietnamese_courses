import sys


if(len(sys.argv) != 2):
    print("wrong number of arguments")
    sys.exit
filename = sys.argv[1]
filename = str(filename).rstrip()
f = open(filename, "r")
baseName = filename.split(".")[0]
extension = filename.split(".")[1]
f2 = open(baseName+"2."+extension, "w")
for line in f:
    if "bogach/prof-courses" in line:
        print(line)
        line = line.replace("bogach/prof-courses",
                            "sonluuxuan/vietnamese_courses")
        print(line)
    f2.write(line)
