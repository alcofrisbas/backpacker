#include <stdio.h>
#include <stdlib.h>
#include "stack.c"
#include "tile.c"


/*
 * testing basic stack functions
 * paired with tile !!! so progrs
 * TODO: pop on empty...
 */

int main(void) {
    Tile *t = newTile();
    Tile *n;
    push(t->head, 5);
    push(t->head, 5);
    push(t->head, 5);
    push(t->head, 6);

    n = walk(t, 0);
    push(n->head, 10);

    n = walk(n, 3);
    printf("%d\n", pop(n->head));
    // for (int i=0; i<10;i ++){
    //     pop(n->head);
    // }
    tileFree(t);
    return 0;
}
