import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url: ')
xml = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

# parses XML from a string directly into the root Element of the parsed tree.
root = ET.fromstring(xml)

# use an XPath selector string look through the entire tree of XML for any tag named 'count'
lst = root.findall('.//count')
print('Count:', len(lst))

total = 0
for item in lst:
    total = total + int(item.text)  # within item, grab the text content
print('Sum:', total)
