import re
import argparse

parser = argparse.ArgumentParser(description="Removes shit from ripped books")
parser.add_argument("-i", "--input", help="inputfile.txt")
parser.add_argument("-o", "--output", help="outputfile.md")
args = parser.parse_args()



fileopen = open(args.input, "r")

text = fileopen.read()

triple_underscore_re = re.compile(r'_{3}')
text = re.sub(triple_underscore_re, "_ ", text)

underscore_to_bolt_re = re.compile(r'((._)+)')
text = re.sub(underscore_to_bolt_re, r'**\1**', text)

underscore_to_nil_re = re.compile(r'_')
text = re.sub(underscore_to_nil_re, "", text)

out = open(args.output, "w")
out.write(text)