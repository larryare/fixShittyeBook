import re
import argparse

parser = argparse.ArgumentParser(description="Removes shit from ripped books")
parser.add_argument("-i", "--input", help="inputfile.txt")
parser.add_argument("-o", "--output", help="outputfile.md")
args = parser.parse_args()



fileopen = open(args.input, "r")

text = fileopen.read()

text = text.replace("<I>", "")
text = text.replace("</I>", "")

text = text.replace("___", " ")

underscore_to_bold_re = re.compile(r'[^_](?:_[^_])+')
text = re.sub(underscore_to_bold_re, r'**\g<0>**', text)

text = text.replace("_", "")

out = open(args.output, "w")
out.write(text)