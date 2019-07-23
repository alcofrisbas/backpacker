# backpackr

backpackr is an esoteric language designed with a whimsical take in mind. It is a travelling/boardgame themed language based solely in stacks.

the backpacker is a pointer that operates on an unlimited two-dimensional plane of stacks and carries a backpack, which is also a stack. Among other things, he can place things on the stack he is standing on, as well as look at things and print to stdout.

In this repo, there is a sloppily-written interpreter for backpackr.

|Command|Action|
|---|---|
|w|move up(on the 2d ground)|
|a|move left|
|s|move down|
|d|move right|
|p|put a number down(takes int argument), on empty, put top bag item onto ground. ignore if the bag is empty|
|l|"look" at an object on the ground and put it into the bag|
|e|empty the contents of the bag onto stdout|
|g|empty the contents of the bag onto the ground|
|c|combine(by addition) the top item in the backpack with the top item on the ground|
|r|combine(by subtraction) the same|
|t|tip out the first item in the backpack onto the stdout|
|f|the conditional. Compares the top item of the backpack with the top item on the ground. if there is no match, it skips to the next line|
|v| takes argument integer. jump down n lines|
|^| takes argument integer. jump up n lines|
|m| takes a single integer argument and puts into the backpack|



Note: e will print out ascii form of the number unless the number is preceded by a zero.

For example:

```
p10lp100lp108lp114lp111lp119lp32lp44lp111lp108lp108lp101lp104le
```
prints "hello, world" to standard out, and


is a counter that counts to 10:
```
p0p1lcwcwsslcp0lep10le
wlcsclcp0lep10lelc
p10fv2
^2

```
the extra newline is important at the end.

```
p100p1lrwcwsslcp0lep10le
wlcs"r"<-SUBTRACT lcp0lep10lelc
p0fv2
^2

```
The above code demonstrates how comments work. Any characters that are not numbers or in the above text are ignored and do not trigger errors. By convention, using all caps for comments makes them easier to read, and using arrows and quotations marks is helpful for being precise in explanation. The above code prints the numbers 99 to 0 to standard out. As the language expands, more capital letters will be used as keywords, so a safer way to comment out a line is the following:

```
v0 This is a comment. all chars in this line are ignored
```

### Fibonacci Sequence

The first program enumerates the fibonacci sequence until reaching 144. The second one endlessly enumerates it

```
ap0dp1
alcp0le
dlcp0lp10le
lcacwgslcp0lp10le
lcp144fv3
lcdcwgslcp0lp10le
lcp144fv1
^4
p10le
```
```
ap0dp1
alcp0le
dlcp0lp10le
lcacwgslcp0lp10le
lcdcwgslcp0lp10le
^2
p10le
```

### Quasi-functions

One way to streamline or de-clutter code is to use code from another file. The following commands help with executing functions. This enables your backpacker to follow a different path over the same terrain of stacks without using a myriad of jump commands that need to be changed every time a line is inserted.

|Command|Action|
|---|---|
|x| reads characters from the backpack and looks for a file with that name. the child file is immediately tokenized and executed over the same ground as the parent file.|
|h| go to 'home' (0,0)|

Just like assembly languages and hiking in the woods, it's very polite to leave the terrain as you found it. A conscientious child file should consume its input and refrain from dumping its integer waste all around in different stacks, as well as leaving the backpack just way it found it. Below is an example of two programs that add two integers and print the output.

m.bpkr
```
ap20ddp3
ap97lx
p10llp0le
```
a.bpkr
```
alddck
lap
h
```


```m``` loads two integers into two stacks, then calls ```a```. ```a``` looks for two integers in designated stacks, adds them together, then places them at home. After ```a``` is done, ```m``` looks at home for the return value, then prints whatever is there. ```a``` is a conscientious function because it consumes its arguments, returns a value to home, and does nothing else to alter its surroundings.

### (Tail)Recursion

Using ```x```, a file can call itself, but issues arise if the recursion needs a conditional stop; any variables created in a file will be re-created when it is called again. Using a helper file for this purpose is pretty useful. See the following code, which prompts the user for a number, then prints out the first n numbers in the fibonacci sequence using a function that calls itself.

hf.bpkr
```
wap1dp0ssamp v0 INITIATE CONDITIONAL VALUES AND ITERATOR
hap0ddp1     v0 SETUP FIB
hp102lx      v0 CALL F
```
f.bpkr
```
hwlcssalcpfv6 v0 CHECK CONDITIIONAL
hwalcdck      v0INCREMENT COUNTER
hp10lalcp0lelcddckh v0 PRINT AND ADD(QUASI N-TWO)
wlcssalcpfv3  v0 CHECK CONDITIIONAL
hwalcdck      v0 INCREMENT COUNTER
hp10ldlcp0lelcaackh v0 PRINT AND ADD(QUASI N-ONE)
p102lx v0 PRINT HI & CALL SELF

```

The reason why this function is questionable is because of how 'variables' work in backpacker. A good way to create a variable is to pick a location and stockpile integers there, just like a squirrel in fall. Then, when the information is needed again, the backpacker can go to that location and access it. The consequence of this is that there is no scope whatsoever.

Using common sense, I gave ```hf``` 4 stacks north and south of home and reserved the stacks directly to the east and west for ```f```'s computation. A polite program does this. It is nice to respect boundaries, even if you can step right over them.

However, on first glance, this implementation steps over minor boundaries. Each it's called, ```f``` looks at variables that ```hf```  originally initiated, information 'owned' by ```hf```. This is a violation! Well, actually, it's not. The recursive method of generating the fibonacci sequence uses parameters. This apparent breach of privacy is actually just ```f``` taking the previous two fibonacci numbers and a counter, just like any other recursive implementation of the fibonacci sequence.

### More flow controls

a ```.```(dot) followed by a number ```n``` will repeat code ```n``` times until the next dot. ```.5p101lt.p10lt``` will write 5 ```e```s to the terminal. 

The symbol ```?``` peeks the the top item in the backpack. If the backpack is empty ```?``` evaluates to 0.  ```p5l.?p101lt.p10lt``` will also write 5 ```e```s to the terminal.
