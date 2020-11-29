import re
import argparse
import pypandoc

parser = argparse.ArgumentParser(description="Removes shit from ripped books")
parser.add_argument("input", help="inputfile.txt")
parser.add_argument("-t", "--title", help="Book title")
parser.add_argument("-y", "--year", help="Release year")
parser.add_argument("-a", "--author", help="Author")
args = parser.parse_args()

lst = {
    'à': 'ą',
    'À': 'Ą',
    'è': 'č',
    'È': 'Č',
    'æ': 'ę',
    'Æ': 'Ę',
    'ë': 'ė',
    'Ë': 'Ė',
    'á': 'į',
    'Á': 'Į',
    'Ð': 'Š',
    'ð': 'š',
    'û': 'ū',
    'Û': 'Ū',
    'ø': 'ų',
    'Ø': 'Ų',
    'þ': 'ž',
    'Þ': 'Ž'
}

fileopen = open(args.input, "r")

text = fileopen.read()

fileopen.close()

lines = text.splitlines()

for key in lst.keys():
    text = text.replace(key, lst[key])

title = "error"
if args.title == None:
    title = lines[0]
else:
    title = args.title

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

out = open("{}.md".format(title), "w", encoding="utf-8")
out.writelines(["% {}\n".format(args.title), "% {}\n".format(args.author), "% {}\n".format(args.year)])
out.write(text)
out.close()

output = pypandoc.convert_file("{}.md".format(title), "epub", outputfile="{}.epub".format(title))
