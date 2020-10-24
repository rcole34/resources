#! /bin/bash
cp remoteconfig.template.json config.json
echo "updating last updated config params"
jq -c '.[]' modified_files.json | while read i; do
	if [[ $i = \"act.json\" ]]
	then
		echo "updating act"
		jq '.parameterGroups.lastUpdated.parameters.actResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	elif [[ $i = \"shop.json\" ]]
	then
		echo "updating shop"
		jq '.parameterGroups.lastUpdated.parameters.shopResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	elif [[ $i = \"educate.json\" ]]
	then
		echo "updating educate"
		jq '.parameterGroups.lastUpdated.parameters.educateResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	elif [[ $i = \"advocate.json\" ]]
	then
		echo "updating advocate"
		jq '.parameterGroups.lastUpdated.parameters.advocateResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	elif [[ $i = \"today.json\" ]]
	then
		echo "updating today"
		jq '.parameterGroups.lastUpdated.parameters.todayResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	elif [[ $i = \"states/*.json\" ]]
	then
		echo "updating local"
		jq '.parameterGroups.lastUpdated.parameters.localResourcesLastUpdated.defaultValue.value = $timestamp' --arg timestamp $(date +%s) config.json > tmp.json && mv tmp.json config.json
	fi
done
mv config.json remoteconfig.template.json
