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
	  DOT/STOP: loop flow
"""
def tokenize(s, debug=False):
	l = []
	x = 0
	loop = []
	while x < len(s):
		char = s[x]
		if char in "wasdlptecrg\nv^fmhxkuz":
			l.append(Token("KW",char))
		elif char == ".":
			#l.append(Token("DOT",char))
			if x < len(s)-1:
				if s[x+1].isdigit():
					l.append(Token("DOT", char))
				else:
					l.append(Token("STOP", char))
		elif char.isdigit():
			n = char
			x += 1
			while x < len(s) and s[x].isdigit():
				n += s[x]
				x += 1
			l.append(Token("N",n))
			x -= 1

		x += 1
	if debug:
		for i in l:
			print(i)
	return l

"""
Parse and evaluate a list of tokens
Tried to keep the number of times errors resulted in program
termination.
The main goal is to respond to errors by doing absolutely nothing.
Characters that are neither numbers or commands are ignored and
can be used as comments
commands: w a s d f e t l p c r g v ^ m x k u z h
"""
def setup():
	location = [0,0]
	backpack = []
	ground = {}
	return location, backpack, ground
def parseEval(l, location, backpack, ground,x):
	lookedAt = l
	loop = 0
	while x < len(l):
		w = l[x]
		# loop
		if w.t == "DOT":
			loop += 1
			times = l[x+1]
			if times.t != "N":
				continue
			times = int(l[x+1].v)
			y = x+1
			# get code to execute
			while y < len(l) and loop > 0:
				if l[y].t == "DOT":
					loop += 1
				if l[y].t == "STOP":
					loop -= 1
				y += 1
			# execute it times times
			for i in range(times-1):
				parseEval(l[x+2:y-1], location,backpack, ground, 0)
			x += 1
		# keyword handling
		if w.t == "KW":
			#movement
			if w.v == "w":
				location[1] = location[1]+1
			elif w.v == "s":
				location[1] = location[1]-1
			elif w.v == "d":
				location[0] = location[0]+1
			elif w.v == "a":
				location[0] = location[0]-1
			elif w.v == "h":
				location[0] = 0
				location[1] = 0
			# put command
			elif w.v == "p":
				x += 1
				# edge case: p as the last char
				if x >= len(l):
					if len(backpack) > 0:
						p = backpack.pop()
				# if next token is not an int
				elif l[x].t != "N":
					if len(backpack) > 0:
						p = backpack.pop()
						x-=1
					else:
						x -= 1
						continue
				else:
					p = l[x].v
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					ground["{},{}".format(str(location[0]),str(location[1]))] = []
				ground["{},{}".format(str(location[0]),str(location[1]))].append(p)
			# jump down
			elif w.v == "v":
				x += 1
				if x >= len(l):
					continue
				if l[x].t != "N":
					p = 1
				else:
					p = int(l[x].v) + 1
				for i in range(p):
					while l[x].v != "\n":
						x += 1
					x += 1
				x -= 1
			# jump down
			elif w.v == "^":
				x += 1
				if x >= len(l):
					continue
				if l[x].t != "N":
					p = 1
				else:
					p = int(l[x].v) + 1
				for i in range(int(l[x].v)+1):
					while x > 0 and l[x].v != "\n":
						x -= 1
					x -= 1
				x -= 1
			# look
			elif w.v == "l":
				if ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					try:
						p = ground["{},{}".format(str(location[0]),str(location[1]))].pop()
						backpack.append(p)
					except:
						pass
			# print 1
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
			# print all
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
			# empty on spot
			elif w.v == "g":
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
						ground["{},{}".format(str(location[0]),str(location[1]))] = []
				while len(backpack) > 0:
					ground["{},{}".format(str(location[0]),str(location[1]))].append(backpack.pop())
			# add
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
					pass
			# subtract
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
					pass
			# conditional
			elif w.v == "f":
				p = backpack.pop()
				if str(p) != str(ground["{},{}".format(str(location[0]),str(location[1]))].pop()):
					while l[x].v != "\n":
						x += 1
			# input data
			elif w.v == "m":
				s = input("")
				if s.isdigit():
					backpack.append(s)

			# execute file
			elif w.v == "x":
				#print("--x--")
				lst = []
				while len(backpack) > 0:
					lst.append(backpack.pop())

				lst = [chr(int(i)) for i in lst]
				fname = "".join(lst)+".bpkr"
				#print(fname)
				with open(fname) as r:
					text = r.read()
				tkns = tokenize(text)

				location, backpack, ground = parseEval(tkns, location, backpack, ground,0)
			# delete backpack
			elif w.v == "k":
				del backpack[:]
			# check if ground is empty
			elif w.v == "u":
				if ground.get("{},{}".format(str(location[0]),str(location[1])),False) and len(ground["{},{}".format(str(location[0]),str(location[1]))]) != 0:
					while l[x].v != "\n":
						#print(l[x])
						x+=1
					x+=0
			# empty ground underneath pointer
			elif w.v == "z":
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					pass
				else:
					while len(ground["{},{}".format(str(location[0]),str(location[1]))]) > 0:
						y = ground["{},{}".format(str(location[0]),str(location[1]))].pop()
			else:
				pass
		x += 1
		#print(w.v, ground)
	return location, backpack, ground


if __name__ == '__main__':
	with open(sys.argv[1]) as r:
		s = r.read()
	debug = False
	if len(sys.argv)==3 and sys.argv[2] == "-d":
		debug = True
	location, backpack, ground = setup()
	location, backpack, ground = parseEval(tokenize(s, debug=debug),location,backpack, ground,0)
	if debug:
		print(ground)
