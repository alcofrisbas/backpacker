#include <stdio.h>
#include <stdlib.h>
#include "tile.c"

/* deprecated: tiles now have stacks */

int main(void){
    Tile *t = newTile();
    Tile *n;
    printTile(t);
    n = walk(t, 2);
    printTile(n);
    n = walk(n, 0);
    printTile(n);
    n = walk(n, 1);
    printf("%d\n", connected(n, t));

    printTile(t);
    printTile(n);
    tileFree(t);
    return 0;
}
