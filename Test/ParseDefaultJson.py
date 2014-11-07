import json
twitterExample = open("default.json", "r")
twitterString = twitterExample.read()
parsedJson = json.loads(twitterString)
#prints the ID tag
print parsedJson["id"];
#locates the data 
dataContainer = parsedJson["data"];
print(dataContainer["content"]);
