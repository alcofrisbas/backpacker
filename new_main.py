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
        self.ground = {}
        self.ptr = 0

    def evaluate(self):
        self.parseEval(self.l, 0,0)
        if self.debug:
            print(self.ground)

    def setS(self, s):
        self.s = s

    def setDebug(self, d):
        self.debug = d

    def tokenize(self):
        print(self.debug)
        x = 0
        while x < len(self.s):
            char = self.s[x]
            if char in "wasdlptecrg\nv^fmhxkuz":
                self.l.append(Token("KEY",char))
            elif char == ".":
                #l.append(Token("DOT",char))
                if x < len(self.s)-1:
                    if self.s[x+1].isdigit():
                        l.append(Token("DOT", char))
                    else:
                        l.append(Token("STOP", char))
            elif char == "?":
                self.l.appent(Token("STAR", 0))
            elif char.isdigit():
                n = char
                x += 1
                while x < len(self.s) and self.s[x].isdigit():
                    n += self.s[x]
                    x += 1
                self.l.append(Token("NUM",n))
                x -= 1

            x += 1
        if self.debug:
            for i in self.l:
                print(i)

    def exists(self):
        return self.ground.get("{},{}".format(str(self.location[0]),str(self.location[1])),False)

    def make(self):
        if not self.exists():
            self.ground["{},{}".format(str(self.location[0]),str(self.location[1]))] = []

    def put(self, p):
        self.make()
        self.ground["{},{}".format(str(self.location[0]),str(self.location[1]))].append(p)

    def parseEval(self, l, ptr loop):
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
        if w.t == "DOT":

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
                if ptr >= len(l):
                    if len(self.backpack) > 0:
                        p = backpack.pop()
                elif l[ptr].t not in ["NUM", "STAR"]:
                    if len(backpack) > 0:
                        p = backpack.pop()
                        ptr -= 1
                    else:
                        ptr -= 1
                else:
                    p = l[ptr].v
                self.put(p)
                return self.parseEval(l, ptr+1, loop)

if __name__ == '__main__':
    interpreter = Interpreter()
    interpreter.setS("wwwp100")
    interpreter.setDebug(True)
    interpreter.tokenize()
    interpreter.evaluate()
