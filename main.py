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
		if char in "wasdlptecrg\nv^fmhxkuz":
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
commands: w a s d f e t l p c r g \n v ^ m
"""
def setup():
	location = [0,0]
	backpack = []
	ground = {}
	return location, backpack, ground
def parseEval(l, location, backpack, ground,x):
	#location = [0,0]
	#backpack = []
	#ground = {}
	#x = 0
	#print(len(l))
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
			elif w.v == "h":
				location[0] = 0
				location[1] = 0
				#print(location)
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
				"""print("m")
				c = getch()
				while c == " ":
					print("space")
					c = getch()
				s = ""
				while c != "\n":
					print("chars")
					print(c)
					if c == " ":
						print("'"+s+"'")
						if s.isdigit():
							backpack.append(s)
							s = ""
							continue
						print("improper input")
						sys.exit(1)
					s += c
					c = getch()"""
				s = input("")
				if s.isdigit():
					backpack.append(s)
				
			
			elif w.v == "x":
				#print("--x--")
				lst = []
				while len(backpack) > 0:
					lst.append(backpack.pop())
				
				lst = [chr(int(i)) for i in lst]
				fname = "".join(lst)+".backpack"
				#print(fname)
				with open(fname) as r:
					text = r.read()
				tkns = tokenize(text)
				#print tkns
				#print(ground)
				location, backpack, ground = parseEval(tkns, location, backpack, ground,0)
				#print(ground)
				#print(backpack)
				for i in tkns:
					pass#print(i)
				#print("")
				for i in l:
					pass#print(i)
				#print(len(l))
			elif w.v == "k":
				del backpack[:]

			elif w.v == "u":
				if ground.get("{},{}".format(str(location[0]),str(location[1])),False) and len(ground["{},{}".format(str(location[0]),str(location[1]))]) != 0:
					#print("full b")
					while l[x].v != "\n":
						#print(l[x])
						x+=1
					#print(l[x])
					x+=0
				#print(len(l),x)

			elif w.v == "z":
				#print("deleting", location)
				if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					pass
				else:
					#print("notPass")
					while len(ground["{},{}".format(str(location[0]),str(location[1]))]) > 0:
						y = ground["{},{}".format(str(location[0]),str(location[1]))].pop()
			else:
				pass
		#print("next")
		x += 1
	# For debugging Code:	
	#print(ground)
	#print(backpack)
	#print(len(l))
	return location, backpack, ground


if __name__ == '__main__':
	with open(sys.argv[1]) as r:
		s = r.read()
	location, backpack, ground = setup()
	location, backpack, ground = parseEval(tokenize(s),location,backpack, ground,0)






