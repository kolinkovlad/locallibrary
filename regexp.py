import re

text = """In September 1769 she reached New
Zealand, the first European vessel to visit
in 127 years."""

print(text)
m = re.search('i', text)
print(m.group(), m.start(), m.end())

# m = re.finditer('i', text)
# for i in m:
#     print("’{0}’: {1}-{2}".format(i.group(), i.start(), i.end()))


# s = "text1, text2, textЗ text4"
#
# p = re.compile(r"\w+(?=[,])", re.S | re.I)
# print(p.findall(s))