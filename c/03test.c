#include <stdio.h>
#include <stdlib.h>
#include "tile.c"
#include "stack.c"

int main(void) {
    StackValue *s = newStack();
    push(s, 1);
    push(s, 2);
    push(s, 3);
    printf("%d\n",pop(s));
    push(s, 4);
    printStack(s);
    freeStack(s);
    return 0;
}
