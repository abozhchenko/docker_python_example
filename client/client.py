#!/usr/bin/env pyrhon3
import urllib.request
fp = urllib.request.urlopen("http://localhost:1234/")
encodedContent=fp.read()
decodedContent=encodedContent.decode("utf8")
#encodedContent=fp.encode()
print(decodedContent)
fp.close()