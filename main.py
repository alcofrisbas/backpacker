"""
Backpacker language
Written Late February 2018
by Ben Greene
"""
import sys
class Token:
	def __init__(self,t, v):
		self.t = t
		self.v = v
	def __str__(self):
		return "{}\t{}".format(self.t, self.v)
"""
Tokenize input string and return a list of typed tokens
Type: KW: keyword
      N:  number
"""
def tokenize(s):
	l = []
	x = 0
	while x < len(s):
		char = s[x]
		if char in "wasdlptecrg\nv^fm":
			l.append(Token("KW",char))
		if char.isdigit():
			n = char
			x += 1
			while x < len(s) and s[x].isdigit():
				n += s[x]
				x += 1
			l.append(Token("N",n))
			x -= 1

		x += 1
	return l
"""
Parse and evaluate a list of tokens
Tried to keep the number of times errors resulted in program
termination.
The main goal is to respond to errors by doing absolutely nothing.
Characters that are neither numbers or commands are ignored and
can be used as comments
commands: w a s d f e t l p c r g \n v ^
"""
def parseEval(l):
	location = [0,0]
	backpack = []
	ground = {}
	x = 0
	lookedAt = l
	while x < len(l):
		w = l[x]
		if w.t == "KW":
			if w.v == "w":
				location[1] = location[1]+1
			elif w.v == "s":
				location[1] = location[1]-1
			elif w.v == "d":
				location[0] = location[0]+1
			elif w.v == "a":
				location[0] = location[0]-1
			elif w.v == "p":
				x += 1
				if l[x].t != "N":
					if len(backpack) == 0:
						continue
					else:
						p = backpack.pop()
				else:
					p = l[x].v
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					ground["{},{}".format(str(location[0]),str(location[1]))] = []
				ground["{},{}".format(str(location[0]),str(location[1]))].append(p)
			elif w.v == "v":
				x += 1
				if l[x].t != "N":
					print("error")
					sys.exit(1)
				else:
					for i in range(int(l[x].v)+1):
						while l[x].v != "\n":
							x += 1
						x += 1
				x -= 1

			elif w.v == "^":
				x += 1
				if l[x].t != "N":
					print("error")
					sys.exit(1)
				else:
					for i in range(int(l[x].v)+1):
						while x > 0 and l[x].v != "\n":
							x -= 1
						x -= 1
				x -= 1

			elif w.v == "l":
				if ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					try:
						p = ground["{},{}".format(str(location[0]),str(location[1]))].pop()
						backpack.append(p)
					except:
						pass
			elif w.v == "t":
				try:
					c = backpack.pop()
					if int(c) != 0:
						sys.stdout.write(chr(int(c)))
					else:
						try:
							c = backpack.pop()
							sys.stdout.write(str(int(c)))
						except:
							sys.stdout.write("0")
					sys.stdout.flush()
				except:
					print("fail")
			elif w.v == "e":
				while len(backpack) > 0:
					c = backpack.pop()
					if int(c) != 0:
						sys.stdout.write(chr(int(c)))
					else:
						try:
							c = backpack.pop()
							sys.stdout.write(str(int(c)))
						except:
							sys.stdout.write("0")
					sys.stdout.flush()
			elif w.v == "g":
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
						ground["{},{}".format(str(location[0]),str(location[1]))] = []
				while len(backpack) > 0:
					ground["{},{}".format(str(location[0]),str(location[1]))].append(backpack.pop())
			elif w.v == "c":
				try:
					p = backpack.pop()
					if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
						ground["{},{}".format(str(location[0]),str(location[1]))] = []
					if ground["{},{}".format(str(location[0]),str(location[1]))] == []:
						ground["{},{}".format(str(location[0]),str(location[1]))].append(p)
					else:
						ground["{},{}".format(str(location[0]),str(location[1]))][-1] = str(int(ground["{},{}".format(str(location[0]),str(location[1]))][-1])+int(p))
					backpack.append(p)	
	
				except:
					print("combination error")
					sys.exit(1)
			elif w.v == "r":
				try:
					p = backpack.pop()
					if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
						ground["{},{}".format(str(location[0]),str(location[1]))] = []
					if ground["{},{}".format(str(location[0]),str(location[1]))] == []:
						ground["{},{}".format(str(location[0]),str(location[1]))].append(p)
					else:
						ground["{},{}".format(str(location[0]),str(location[1]))][-1] = str(int(ground["{},{}".format(str(location[0]),str(location[1]))][-1])-int(p))
					backpack.append(p)	

	
				except:
					print("reduction error")
					sys.exit(1)
			elif w.v == "f":
				p = backpack.pop()
				if str(p) != str(ground["{},{}".format(str(location[0]),str(location[1]))].pop()):
					while l[x].v != "\n":
						x += 1
			elif w.v == "m":
				s = input("")
				if s.isdigit():
					backpack.append(s)
			else:
				pass

		x += 1
	# For debugging Code:	
	#print(ground)
	#print(backpack)


if __name__ == '__main__':
	with open(sys.argv[1]) as r:
		s = r.read()
	parseEval(tokenize(s))






