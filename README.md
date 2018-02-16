# backpacker

backpacker is an esoteric language designed with a whimsical take in mind.

the backpacker operates on an unlimited plane of stacks and carries a backpack, which is also a stack. he can pick up and look at items on the ground and put them in his bag. he can also empty the bag out onto stdout.

|Command|Action|
|---|---|
|w|move up(on the 2d ground)|
|a|move left|
|s|move down|
|d|move right|
|p|put a number down(takes int argument)|
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