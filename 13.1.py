import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter file: ')

    if len(url) < 1:
        continue
    print("Retrieving", url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # print(json.dumps(js["comments"], indent=2))
    counter = 0
    for comment in js["comments"]:
        print(comment["count"])
        count = comment["count"]
        counter += count
    print(counter)
    # headers = dict(connection.getheaders())
    # print(headers)
