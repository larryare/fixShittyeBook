import re
import argparse
import pypandoc

parser = argparse.ArgumentParser(description="Removes shit from ripped books")
parser.add_argument("-i", "--input", help="inputfile.txt", required=True)
parser.add_argument("-t", "--title", help="Book title", required=True)
parser.add_argument("-y", "--year", help="Release year")
parser.add_argument("-a", "--author", help="Author")
args = parser.parse_args()



fileopen = open(args.input, "r")

text = fileopen.read()

text = text.replace("<I", "")
text = text.replace("/I>", "")

things_to_subtitle_re = re.compile(r'(?:>)\d*(?:<)')
text = re.sub(things_to_subtitle_re, r'## \g<0>', text)

things_to_title_re = re.compile(r'(?:>)[^0-9]*(?:<)')
text = re.sub(things_to_title_re, r'# \g<0>', text)

text = text.replace(">", "")
text = text.replace("<", "")

text = text.replace("___", " ")

underscore_to_bold_re = re.compile(r'[^_](?:_[^_])+')
text = re.sub(underscore_to_bold_re, r'**\g<0>**', text)

#space_to_italy_re = re.compile(r'[^ ](?: [^ ])+')
#text = re.sub(space_to_italy_re, r'*\g<0>*', text)

text = text.replace("_", "")

out = open("{}.md".format(args.title), "w")
out.writelines(["% {}\n".format(args.title), "% {}\n".format(args.author), "% {}\n".format(args.year)])
out.write(text)

output = pypandoc.convert_file("{}.md".format(args.title), "epub", outputfile="{}.epub".format(args.title))