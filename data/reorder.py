#!/usr/local/bin/python3
# Paul Evans (paul.evans@aya.yale.edu)
# 29 April 2019
#
# reorder.py reorders attributes in <div> tags emitted by Sg.py
#
# 1. Sg.py > input.xml
# 2. open input.xml in Atom, command-shift-X to format XML
# 3. vi input.xml, :set fileformat=unix, :wq
# 4. reorder.py
# 5. open output.xml in Atom, validate XML
# 6. mv output.xml Sg.xml
#
import re
def main():
    with open('input.xml', 'r') as input, open('output.xml', 'w') as output:
        lines = input.readlines()
        for line in lines:
            line = re.sub('(n=\"C\..*?\")\ (subtype=\"case\")\ (type=\"section\")',
            r'\3 \2 \1', line)
            line = re.sub('(n=\"C\..*?\ d\.init\.\")\ (subtype=\"dictum\")\ (type=\"textpart\")',
            r'\3 \2 \1', line)
            line = re.sub('<ab \/>', '<ab></ab>', line)
            output.write(line)

if __name__ == '__main__':
    main()
