import requests
res=requests.get("https://www.gutenberg.org/cache/epub/67650/pg67650.txt")
res.raise_for_status()
playFile = open("The Tales of the Samurai.text","wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()