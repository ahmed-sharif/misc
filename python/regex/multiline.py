import re

paragraph = '''
   <p>
   This is a paragraph.
   It has multiple lines.
   </p>
'''



pattern = r"<p>(.*)</p>"
regex = re.compile(pattern, re.DOTALL)


m = regex.search(paragraph)
print m.group(1)
