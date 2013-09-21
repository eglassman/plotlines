import json

plotline = json.load(open("plotlines2.json"))
chars = json.load(open("characters.json"))

new_format = {}

new_format['panels'] = len(plotline)

scenes = []
oldscene = {"start":0, "duration": 0, "id": -1}
count = 0

def indexOfChar(name):
	for i in range(len(chars)):
		if chars[i]['name'] == name:
			return i
	return -1

for event in plotline:
	scene = {"duration": 1,
			 "start": oldscene['start'] + oldscene['duration'],
			 "id": count}
	count += 1

	scene['chars'] = []
	for act in event['actors']:
		index = indexOfChar(act)
		if index < 0:
			print "Something went terribly wrong" + act
			break
		scene['chars'].append(index)

	scenes.append(scene)

	oldscene = scene

new_format['scenes'] = scenes

with open("reparsed.json", "w") as outfile:
	json.dump(new_format, outfile)