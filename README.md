# backpacker

backpacker is an esoteric language designed with a whimsical take in mind. It is a travelling/boardgame themed language based solely in stacks.

the backpacker is a pointer that operates on an unlimited two-dimensional plane of stacks and carries a backpack, which is also a stack. Among other things, he can place things on the stack he is standing on, as well as look at things and print to stdout. 

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
|x| reads characters from the backpack and looks for a file with that name. the child file is immediately tokenized and executed over the same ground as the parent file.|
|k| destroys the contents of the backpack|
|h| go to 'home', 0,0|

Note: e will print out ascii form of the number unless the number is preceded by a zero.

For example:

```
p10lp100lp108lp114lp111lp119lp32lp44lp111lp108lp108lp101lp104le
```
prints "hello, world" to standard out, and

```
p256p1lcwcwgsslcep10le
wlcsclcep10le
^1
```
is an infinitely looping counter starting at 1, and the following is counter that counts to 10:
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
The above code demonstrates how comments work. Any characters that are not numbers or in the above text are ignored and do not trigger errors. By convention, using all caps for comments makes them easier to read, and using arrows and quotations marks is helpful for being precise in explanation. The above code prints the numbers 99 to 0 to standard out.

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
