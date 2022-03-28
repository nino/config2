from sys import argv
import re

infile = argv[1]
outfile = re.sub(r"\.csv", ".out.csv", infile)

with open(infile, "r") as readfile:
    with open(outfile, "w") as writefile:
        for line in readfile:
            line = re.sub(r"(20\d\d-\d\d-\d\d) \d\d:\d\d:\d\d", "\g<1>", line)
            writefile.write(line)
