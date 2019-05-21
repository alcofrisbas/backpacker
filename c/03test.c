#include <stdio.h>
#include <stdlib.h>
#include "stack.c"
#include "tile.c"


/*
 * testing basic stack functions...
 * TODO: pop on empty...
 */

int main(void) {
    StackValue *s = newStack();
    push(s, 1);
    push(s, 2);
    push(s, 3);
    printf("%d\n",pop(s));
    printf("%d\n",peek(s));
    push(s, 4);
    printStack(s,1);
    printf("%d\n",peek(s));
    freeStack(s);
    return 0;
}
