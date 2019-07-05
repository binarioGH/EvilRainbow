#-*-coding: utf-8-*-
from time import strftime 
import codecs
#Functions ↓

def banner():
	print('''
		 ____________        _____________
		|    ________|      |     ___    |
		|    |              |    |___|   |    
		|    |_______       |    ___     |
		|    ________|      |   |   \\    \\
		|    |              |   |    \\    \\
		|    |________      |   |     \\    \\   
		|____________|      |___|      \\____\\

		[!] Evil Rainbow

		[!] By Binario

		[?] GitHub: https://github.com/binarioGH ''')

def loadFile(file, split=False):
	try:
		with codecs.open(file, "r", encoding="utf-8") as f:
			content = f.read()
	except Exception as e:
		print(e)
		exit()
	else:
		if split:
			content = content.split()
		return content

#Functions ↑

#Lambdas ↓ 
getDate = lambda: "{}-{}".format(strftime("%d-%m-%y"), strftime("%H-%M-%S"))
#Lambdas ↑