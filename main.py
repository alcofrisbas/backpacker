"""

there is an infite 2d field of stacks. for now, each is
however deep.

commands:

w move up
s move down
a move left
d move right

movements can be multiple to line?

the backpack:
another stack that is essentially output

l(ook) look at something on the ground.
	this puts it in the backpack
p(lace) put something on the ground. followed by an integer
t(ip) put the top item in the backpack stack on the ground
e(mpty) write the backpack to stdout. this empties the backpack.
g(round) empty the backpack onto the ground
c(ombine) put something from the backpack on the ground. if the ground is not empty,
	add the combine the top item and the top backpack item.
r(emove) same as combine, but subtract. if the total is less than 0, then make it 0
v switch tracks. followed by number
g empty the backpack onto the ground
(i)f some sort of conditional statement that involves skipping to the next line 
"""
"""

keeping track...
have coordinates of the user.
use a dictionary for each stack.
just use a python list (pop,push)
have a backpack list that does the same.

need a way to loop!! i'll figure it out later.

"""
import sys
class Token:
	def __init__(self,t, v):
		self.t = t
		self.v = v
	def __str__(self):
		return "{}\t{}".format(self.t, self.v)

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


	for i in l:
		pass#print(i)
	return l

def next(l):
	location = [0,0]
	backpack = []
	ground = {}
	x = 0
	lookedAt = l
	while x < len(l):
		#print(x)
		w = l[x]
		#print(w)
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
				#print("skip")
				x += 1
				if l[x].t != "N":
					print("error")
					sys.exit(1)
				else:
					for i in range(int(l[x].v)+1):
						#print(i)
						while l[x].v != "\n":
							#print("asdf",l[x].v)
							x += 1
						x += 1
				#print("done")
				x -= 1

			elif w.v == "^":
				#print("skip")
				#soFar = lookedAt[0:x]
				#print(soFar)
				x += 1
				if l[x].t != "N":
					print("error")
					sys.exit(1)
				else:
					for i in range(int(l[x].v)+1):
						#print(i)
						while x > 0 and l[x].v != "\n":
							#print ("- time",x)
							#print("asdf",l[x].v)
							x -= 1
						x -= 1
				#print("done")
				x -= 1

			elif w.v == "l":
				#print("looking")
				if ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					try:
						#print("trying")
						#print("pushing {}".format(ground["{},{}".format(str(location[0]),str(location[1]))].pop()))
						p = ground["{},{}".format(str(location[0]),str(location[1]))].pop()
						#print(p)
						backpack.append(p)
					except:
						pass
			elif w.v == "t":
				#print ("tip")
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
					# if not ground.get("{},{}".format(str(location[0]),str(location[1])),False):
					# 	ground["{},{}".format(str(location[0]),str(location[1]))] = []
					# ground["{},{}".format(str(location[0]),str(location[1]))].append(p)
				except:
					print("fail")
			elif w.v == "e":
				#print("writing")
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
				#print("ground")
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
				#print("if")
				p = backpack.pop()
				if str(p) != str(ground["{},{}".format(str(location[0]),str(location[1]))].pop()):
					while l[x].v != "\n":
						#print("asdf",l[x].v)
						x += 1
			elif w.v == "m":
				s = input("")
				#print("s:{}".format(s))
				if s.isdigit():
					#print(True)
					backpack.append(s)
			else:
				pass

		x += 1
		#print (location)
		
		#print(ground)
		#print(backpack)
		#notMatter = input("")
	
	#print("")
	#print(lookedAt[0:x])
	#print(ground)
	#print(backpack)


if __name__ == '__main__':
	#next(tokenize("""p10lp100lp108lp114lp111lp119lp32lp44lp111lp108lp108lp101lp104le"""))
	#next(tokenize("""v2
	#	p111lp104le
	#	p105lp104le"""))


	# infinite print hi loop
	#next(tokenize("""p10lp105lp104le
	#	^1"""))

	#counter print loop(inifinite)
	#next(tokenize("""p0p1lcwcwgsslcep10le
	#	wlcsclcep10le
	#	^1
	#	"""))
	#printing a number: escape by putting a zero right infront of it
	#next(tokenize("""p100lp0lp100le"""))
	#next(tokenize("""p100lp10fp101le
	#	gp100le
	#	p10le"""))

	# next(tokenize("""
	# 	p0p1lcwcwsslcp0lep10le
	# 	wlcsclcp0lep10lelc
	# 	p10fv2
	# 	^2

	# 	"""))
	# next(tokenize("""
	# 	p100p1lrwcwsslcp0lep10le
	# 	wlcs"r"<-SUBTRACT lcp0lep10lelc
	# 	p0fv2
	# 	^2

	# 	"""))
	# next(tokenize("""p10lme"""))

	with open(sys.argv[1]) as r:
		s = r.read()
	next(tokenize(s))






