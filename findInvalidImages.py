#! /usr/bin/python3

import json
import urllib.request
import urllib.error

# Script to find image urls that are no longer valid
print("reading from learn, act, and shop resources")
learnFile = open('./learn.json')
actFile = open('./act.json')
shopFile = open('./shop.json')

learnResources = json.load(learnFile)
actResources = json.load(actFile)
shopResources = json.load(shopFile)

allResources = learnResources + actResources + shopResources
invalidImageCount = 0

print("searching for expired images")
for resource in allResources:
    if "imageUrl" in resource.keys():
        try:
            code = urllib.request.urlopen(urllib.request.Request(resource["imageUrl"], method="HEAD")).getcode()
            if code == 404:
                print("Found invalid image: " + resource["title"] + " (" + resource["imageUrl"] + ")")
                invalidImageCount += 1

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("Found invalid image: " + resource["title"] + " (" + resource["imageUrl"] + ")")
                invalidImageCount += 1

        except urllib.error.URLError as e:
            print("URL error: " + resource["title"] + " (" + resource["imageUrl"] + ")")
            invalidImageCount += 1 

    if "products" in resource.keys():
        for product in resource["products"]:
            if "imageUrl" in product.keys():
                try:
                    code = urllib.request.urlopen(urllib.request.Request(product["imageUrl"], method="HEAD")).getcode()
                    if code == 404:
                        print("Found invalid image: " + product["name"] + " from " + resource["title"] + " (" + product["imageUrl"] + ")")
                        invalidImageCount += 1

                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        print("Found invalid image: " + product["name"] + " from " + resource["title"] + " (" + product["imageUrl"] + ")")
                        invalidImageCount += 1 

                except urllib.error.URLError as e:
                    print("URL error: " + product["name"] + " from " + resource["title"] + " (" + product["imageUrl"] + ")")
                    invalidImageCount += 1 
	
learnFile.close()
actFile.close()
shopFile.close()
print("done! found " + str(invalidImageCount) + " invalid images")

