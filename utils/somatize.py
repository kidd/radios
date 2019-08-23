from lxml import etree
import requests

url = "http://somafm.com/channels.xml"


channels = etree.fromstring(requests.get(url).text.encode('utf8'))

pls_tags = ['highestpls', 'fastpls']

for channel in channels:
    uid = channel.attrib['id']
    plss = filter(
        lambda p: p is not None,
        map(lambda tag: channel.find(tag), pls_tags)
    )
    pls = next(plss, None)
    print("Downloading", pls.text)
    pls_data = requests.get(pls.text)
    pls_file = open(f'{uid}.pls', 'wb')
    pls_file.write(pls_data.content)
    pls_file.close()
