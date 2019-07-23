import sys

class Token:
    def __init__(self,t, v):
        self.t = t
        self.v = v
    def __str__(self):
        return "{}\t{}".format(self.t, self.v)

class Interpreter:
    def __init__(self):
        self.s = ""
        self.l = []
        self.debug = False

        self.location = [0,0]
        self.backpack = []
        self.earth = {}
        self.ptr = 0

    def evaluate(self):
        self.parseEval(self.l, 0,0)
        if self.debug:
            print(self.earth)
            print(self.backpack)

    def setS(self, s):
        self.s = s

    def setDebug(self, d):
        self.debug = d

    def tokenize(self, s, fn=False):
        x = 0
        l = []
        while x < len(s):
            char = s[x]
            if char in "wasdlptecrg\nv^fmhxkuzIOG":
                l.append(Token("KEY",char))
            elif char == ".":
                #l.append(Token("DOT",char))
                if x < len(s)-1:
                    if s[x+1].isdigit() or s[x+1] == "?":
                        l.append(Token("DOT", char))
                    else:
                        l.append(Token("STOP", char))
            elif char == "?":
                l.append(Token("STAR", 0))
            elif char.isdigit():
                n = char
                x += 1
                while x < len(s) and s[x].isdigit():
                    n += s[x]
                    x += 1
                l.append(Token("NUM",n))
                x -= 1

            x += 1
        if self.debug:
            for i in l:
                print(i)
        if not fn:
            self.l = l
            return
        return l
    ''' behavior:
        - no key: false
        - empty list: true
        - non-empty list: true
    '''
    def exists(self):
        if isinstance(self.earth.get("{},{}".format(str(self.location[0]),str(self.location[1])),False), list):
            return True
        print(self.earth.get("{},{}".format(str(self.location[0]),str(self.location[1]))))
        return False


    def make(self):
        if not self.exists():
            print("making")
            self.earth["{},{}".format(str(self.location[0]),str(self.location[1]))] = []

    def put(self, p):
        self.make()
        self.ground().append(p)

    # return 'stack' on which ptr is standing
    def ground(self):
        self.make()
        return self.earth["{},{}".format(str(self.location[0]),str(self.location[1]))]

    # pop top item of ground or None
    def retrieve(self):
        self.make()
        if len(self.ground())>0:
            return self.ground().pop()
        return None

    def getBag(self):
        if not self.backpack:
            return None
        return self.backpack.pop()

    def parseEval(self, l, ptr, loop):
        if ptr >= len(l):
            return
        w = l[ptr]
        if w.t == "NUM":
            ptr += 1
            return w.v
        if w.t == "STAR":
            ptr += 1
            if self.backpack:
                return self.backpack[-1]
            else:
                return "0"
        # TODO: implement me
        if w.t == "DOT":
            ptr += 1
            n = self.parseEval([l[ptr]], 0, loop)
            # print(n)
            if n:
                ptr += 1
                # ptr2 = ptr
                l2 = []
                while l[ptr].t != "STOP":
                    l2.append(l[ptr])
                    ptr += 1
                for i in range(int(n)):
                    self.parseEval(l2, 0, loop)
            # print(l[ptr+1].v)
            return self.parseEval(l, ptr+1, loop)

        if w.t == "KEY":
            if w.v == "w":
                self.location[1] = self.location[1]+1
                return self.parseEval(l, ptr+1, loop)
            elif w.v == "s":
               self.location[1] = self.location[1]-1
               return self.parseEval(l, ptr+1, loop)
            elif w.v == "d":
                self.location[0] = self.location[0]+1
                return self.parseEval(l, ptr+1, loop)
            elif w.v == "a":
                self.location[0] = self.location[0]-1
                return self.parseEval(l, ptr+1, loop)
            elif w.v == "h":
                self.location[0] = 0
                self.location[1] = 0
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "p":
                ptr += 1
                if ptr < len(l):
                    # print(l[ptr])
                    n = self.parseEval([l[ptr]], 0, loop)
                    if n:
                        print("from num")
                        self.ground().append(n)
                    else:
                        print("from bag")
                        if self.backpack:
                            self.ground().append(self.backpack.pop())
                else:
                    print("from bag 2")
                    if self.backpack:
                        self.ground().append(self.backpack.pop())
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "l":
                r = self.retrieve()
                if r:
                    self.backpack.append(r)
                # print(l[ptr+1])
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "e":
                print("printing all")
                while len(self.backpack) > 0:
                    c = self.backpack.pop()
                    if int(c) != 0:
                        sys.stdout.write(chr(int(c)))
                    else:
                        try:
                            c = self.backpack.pop()
                            sys.stdout.write(str(int(c)))
                        except:
                            sys.stdout.write("0")
                    sys.stdout.flush()
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "t":
                if self.backpack:
                    c = self.backpack.pop()
                    if int(c) != 0:
                        sys.stdout.write(chr(int(c)))
                    else:
                        try:
                            c = self.backpack.pop()
                            sys.stdout.write(str(int(c)))
                        except:
                            sys.stdout.write("0")
                    sys.stdout.flush()
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "g":
                while len(self.backpack) > 0:
                    self.put()
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "v":
                ptr += 1
                if ptr >= len(l):
                    return
                n = self.parseEval([l[ptr]], 0, loop)
                if not n:
                    n = 1
                    print("BADNESS")
                n = int(n)
                for i in range(n+1):
                    while l[ptr].v != "\n" and ptr < len(l):
                        ptr += 1
                    ptr+=1
                    n -= 1
                return self.parseEval(l, ptr, loop)

            elif w.v == "^":
                ptr += 1
                if ptr >= len(l):
                    return
                n = self.parseEval([l[ptr]], 0, loop)
                if not n:
                    n = 1
                    print("UP BADDNESS")
                n = int(n)
                for i in range(n+1):
                    while l[ptr].v != "\n" and ptr > 0:
                        ptr -= 1
                    n -= 1
                    ptr-=1
                return self.parseEval(l, ptr+1, loop)


            # ===== conditionals ======

            elif w.v == "f":
                if self.getBag() != self.retrieve():
                    while l[ptr].v != "\n":
                        ptr += 1
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "u":
                if self.exists and len(self.ground()) > 0:
                    while l[ptr].v != "\n" and ptr < len(l):
                        ptr += 1
                ptr +=1
                return self.parseEval(l, ptr, loop)

            # =======================================

            elif w.v == "c":
                p = self.getBag()
                if not p:
                    p = 0
                p = int(p)
                s = self.retrieve()
                if not s:
                    s = 0
                s = int(s)
                print(s+p)
                self.ground().append(str(s+p))

                return self.parseEval(l, ptr+1, loop)

            elif w.v == "r":
                p = self.getBag()
                if not p:
                    p = 0
                p = int(p)
                s = self.retrieve()
                if not s:
                    s = 0
                s = int(s)
                self.ground().append(str(max(s-p,0)))

                return self.parseEval(l, ptr+1, loop)

            elif w.v == "m":
                s = input("")
                try:
                    i = int(s)
                    self.backpack.append(s)
                except:
                    pass
                self.parseEval(l, ptr+1, loop)

            elif w.v == "x":
                fn = ""
                while len(self.backpack) > 0:
                    fn += chr(int(self.getBag()))
                fn += ".bpkr"
                with open(fn) as r:
                    text = r.read()
                tkns = self.tokenize(text, fn=True)
                self.parseEval(tkns, 0, loop)

                return self.parseEval(l, ptr+1, loop)

            elif w.v == "I":
                fn = ""
                while len(self.backpack) > 0:
                    fn += chr(int(self.getBag()))

                try:
                    with open(fn) as r:
                       text = r.read()
                       for t in text:
                           self.ground().append(ord(t))
                except:
                    pass
                return self.parseEval(l, ptr+1, loop)


            elif w.v == "O":
                fn = ""
                while len(self.backpack) > 0:
                    fn += chr(int(self.getBag()))

                try:
                    with open(fn,"w") as w:
                        for t in self.ground():
                            w.write(chr(int(t)))
                except:
                    pass

                return self.parseEval(l, ptr+1, loop)

            elif w.v == "h":
                self.location[0] = 0
                self.location[1] = 0
                return self.parseEval(l, ptr+1, loop)

            elif w.v == "G":
                if len(self.ground()) >= 2:
                    loc = self.ground()
                    self.location[1] = loc.pop()
                    self.location[0] = loc.pop()
                return self.parseEval(l, ptr+1, loop)


            else:
                return self.parseEval(l, ptr+1, loop)



if __name__ == '__main__':
    interpreter = Interpreter()
    with open(sys.argv[1]) as r:
        text = r.read()
    # print(text)
    interpreter.setS(text)
    if len(sys.argv) > 2 and sys.argv[2] == "d":
        interpreter.setDebug(True)
    interpreter.tokenize(interpreter.s)
    interpreter.evaluate()
