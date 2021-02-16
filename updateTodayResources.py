#! /usr/bin/python3

import json
import random

# Script to update today.json with a fresh selection of randomly-picked resources, without repeating the same resource twice
print("reading from learn, act, and shop resources")
learnFile = open('./learn.json')
actFile = open('./act.json')
shopFile = open('./shop.json')

learnResources = json.load(learnFile)
actResources = json.load(actFile)
shopResources = json.load(shopFile)

allResources = learnResources + actResources + shopResources
usedResourceIds = set()
dailyResources = dict()

print("picking random resources to use")
for day in range(1, 31):
	dayResources = []
	while len(dayResources) < 2:
		newResource = random.choice(allResources)
		if newResource['id'] not in usedResourceIds:
			usedResourceIds.add(newResource['id'])
			dayResources.append(newResource)
	dailyResources[str(day)] = dayResources

print("writing output to today.json")
todayFile = open('./today.json', 'w')
todayFile.write(json.dumps(dailyResources, indent=2))

todayFile.close()
learnFile.close()
actFile.close()
shopFile.close()
print("done!")