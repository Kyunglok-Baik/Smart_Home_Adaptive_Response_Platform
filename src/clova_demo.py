import os
import sys
import urllib.parse
import urllib.request
from playsound import playsound

client_id = "4H038gEVAdBjiewlhgyq"
client_secret = "FnPysP0YnC"
encText = urllib.parse.quote("Hello")
data="speaker=clara&speed=0&text=" + encText
url = "https://openapi.naver.com/v1/voice/tts.bin"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response=urllib.request.urlopen(request,data=data.encode('utf-8'))
rescode=response.getcode()

if(rescode==200):
	print("TTS mp3 saved")
	response_body = response.read()
	with open('sample.mp3','wb') as f:
		f.write(response_body)
else:
	print("Error code:"+rescode)

playsound('sample.mp3')
