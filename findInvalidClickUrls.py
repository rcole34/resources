#! /usr/bin/python3

import json
import urllib.request
import urllib.error

# Script to find resource urls that are no longer valid
print("reading from learn, act, and shop resources")
learnFile = open('./learn.json')
actFile = open('./act.json')
shopFile = open('./shop.json')

learnResources = json.load(learnFile)
actResources = json.load(actFile)
shopResources = json.load(shopFile)

allResources = learnResources + actResources + shopResources
invalidClickUrlCount = 0

print("searching for invalid resource urls")
for resource in allResources:
    if "clickUrl" in resource.keys():
        try:
            code = urllib.request.urlopen(urllib.request.Request(resource["clickUrl"], method="HEAD")).getcode()
            if code == 404:
                print("Found invalid click url: " + resource["title"] + " (" + resource["clickUrl"] + ")")
                invalidClickUrlCount += 1

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("Found invalid click url: " + resource["title"] + " (" + resource["clickUrl"] + ")")
                invalidClickUrlCount += 1

        except urllib.error.URLError as e:
            print("URL error: " + resource["title"] + " (" + resource["clickUrl"] + ")")
            invalidClickUrlCount += 1

    if "products" in resource.keys():
        for product in resource["products"]:
            if "clickUrl" in product.keys():
                try:
                    code = urllib.request.urlopen(urllib.request.Request(product["clickUrl"], method="HEAD")).getcode()
                    if code == 404:
                        print("Found invalid click url: " + product["name"] + " from " + resource["title"] + " (" + product["clickUrl"] + ")")
                        invalidClickUrlCount += 1

                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        print("Found invalid click url: " + product["name"] + " from " + resource["title"] + " (" + product["clickUrl"] + ")")
                        invalidClickUrlCount += 1 

                except urllib.error.URLError as e:
                    print("URL error: " + resource["title"] + " (" + resource["clickUrl"] + ")")
                    invalidClickUrlCount += 1

	
learnFile.close()
actFile.close()
shopFile.close()
print("done! found " + str(invalidClickUrlCount) + " invalid click urls")

