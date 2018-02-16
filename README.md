# backpacker

backpacker is an esoteric language designed with a whimsical take in mind.

the backpacker operates on an unlimited plane of stacks and carries a backpack, which is also a stack.

the letters `w a s d` move the backpack

the backpacker can put an object on the ground he's standing on `p <integer>`, put an object in his back `l`, empty the backpack onto the ground `g`, and empty the backback onto stdout `e`.

In addition, he can combine the top item in his bag with to top item he's standing on with `c` and `r`, one being addition, the other subtraction.

The characters `v` and `^` followed by a number jump by newlines in the direction they point.

As of now, there is no branching or flow, but that is up next.

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
