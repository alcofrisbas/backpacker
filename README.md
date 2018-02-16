# backpacker

backpacker is an esoteric language designed with a whimsical take in mind.

the backpacker operates on an unlimited plane of stacks and carries a backpack, which is also a stack.

|Command|Action|
|---|---|
|w|move up|
|a|move left|
|s|move down|
|d|move right|
|p|put a number down(takes int argument)|
|l|"look" at an object on the ground and put it into the bag|
|e|empty the contents of the bag onto stdout|
|g|empty the contents of the bag onto the ground|
|c|combine(by addition) the top item in the backpack with the top item on the ground|
|r|combine(by subtraction) the same|
|t|tip out the first item in the backpack onto the ground|
|f|the conditional. Compares the top item of the backpack with the top item on the ground. if there is no match, it skips to the next line|
|v| takes argument integer. jump down n lines|
|^| takes argument integer. jump up n lines|

Note: e will print out ascii form of the number unless the number is preceded by a zero.

For example:

```
p100lp108lp114lp111lp119lp32lp44lp111lp108lp108lp101lp104le
```
prints "hello, world" to standard out, and

```
p256p1lcwcwgsslcep10le
wlcsclcep10le
^1
```
is an infinitely looping counter starting at 1
