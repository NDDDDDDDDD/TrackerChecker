import json
import requests

# Open sourceFile in readOnly mode
file = open("sources.json", "r")
sources = json.loads(file.read())

# Iterate over all the sources
# Iterate over each element in the source file
for source in sources:
    # Corresponding object
    current = sources[source]
    # GET request
    req = requests.get(current['url'])
    # Response as raw text
    res = req.text
    # If the website is down or we encounter an unexpected status code
    if ((current['message']) in res) or req.status_code != 200:
        print(source, "~> Closed or dead <~")
    else:
        print(source, "~> Open:", req.url)

# Don't forget your good manners
file.close
print("Finished scanning")
