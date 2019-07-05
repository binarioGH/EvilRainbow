#-*-coding: utf-8-*-
from hashlib import *
from json import loads, dumps
from optparse import OptionParser as opt
from sys import argv
from lib import *

ALGORITHMS = {
    "sha256": sha256,
    "blake2b": blake2b,
    "sha3_256": sha3_256,
    "sha3_512": sha3_512,
    "sha1": sha1,
    "blake2s": blake2s,
    "sha224": sha224,
    "sha3_224": sha3_224,
    "sha384": sha384,
    "sha512": sha512,
    "md5": md5
}

class EvilRainbow:
	def __init__(self, p):
		self.p = p
		if self.p:
			print("[+]No errors found.\nStarting...")
	def create(self, i, o, alg):
		words = loadFile(i, split=True)
		outcont = {"hashes": {}}
		for word in words:
			hsh = ALGORITHMS[alg](word.encode()).hexdigest()
			outcont["hashes"][hsh] = word
			if self.p:
				print("{}\n{}:{}".format("-"*80,hsh, word))
		try:
			with open(o, "w") as out:
				out.write(dumps(outcont,indent=4))
		except Exception as e:
			print(e)
			return -1
			exit()
		return 0


	def search(self):
		pass

def printAlgs():
	print(" , ".join(ALGORITHMS))

def main():
	op = opt("Usage: %prog [flgas] [values]")
	op.add_option("-p", "--dontprint", action="store_false", dest="print", default=True, help="Use this flag if you want to print what the program is doing.")
	op.add_option("-P", "--printAlgorithms", action="store_true",dest="sa" ,default=False,help="Use this flag to show all the algorithms available.")
	op.add_option("-c", "--create", action="store_true", dest="create", default=False,help="Use this flag if you want to create a Rainbow dictionary.")
	op.add_option("-s", "--search", action="store_true", dest="search", default=False,help="Use this flag if you want to search a hash in a Rainbow dictionary.")
	op.add_option("-i", "--inputFile", dest="input", default="undefined", help="Set input file, it must contain a list with the words that you want to put in your RD. (if you are using --create)")
	op.add_option("-a", "--algorithm", dest="algorithm", default="md5", help="Set what algortihm is goint to be used to create the RDs(md5 by default) (if you are using --create)")
	op.add_option("-o", "--outputFile", dest="output", default="{}.json".format(getDate()), help="Set output file, it will contain your RD. (if you are using --create)")
	op.add_option("-r", "--rainbowDic", dest="rd", default="undefined", help="Set the RD that you want to search in. (if you are using --search)")
	op.add_option("-H", "--hash", dest="hash", default="undefined", help="Define a single hash that you want to search. (if you are using --search)")
	op.add_option("-d", "--hashlist", dest="hashlist", default="undefined", help="Set a list of hashes to search. (if you are using --search)")
	op.add_option("-l", "--log", action="store_true",dest="log",default=False, help="Save a found hashes log. (if you are using --search)")
	op.add_option("-n", "--logname", dest="logname", default="{}.txt".format(getDate()), help="Put a name to your log. (if you are using --search and --log)")
	(o, argv) = op.parse_args()

	if o.sa:
		printAlgs()

	#handle errors ↓

	if o.create and o.search:
		print("You can't use --create and --search.")
		exit()
	elif not o.create and not o.search:
		print("You have to use --create or --search.")
		exit()
	if o.create and o.input == "undefined":
		print("Input file: {}\nOutput file: {}".format(o.input, o.output))
		exit()
	if o.search and (o.rd == "undefined" or (o.hash == "undefined" and o.hashlist == "undefined")):
		print("RD: {}\nHash: {}\nHash list: {}".format(o.rd,o.hash,o.hashlist))
		exit()
	if o.algorithm not in ALGORITHMS:
		print("{} not found in algorithm list.".format(o.algorithm))
		printAlgs()
		exit()

	#handle error ↑
	er = EvilRainbow(o.print)

	if o.create:
		er.create(o.input, o.output, o.algorithm)
	else:
		if o.hashlist == "undefined":
			hashes = [o.hash]
		else:
			hashes = loadFile(o.hashlist, split=True)
			hashes.append(o.hash)
		er.search(hashes)
if __name__ == '__main__':
	banner()
	main()