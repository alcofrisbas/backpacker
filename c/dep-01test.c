#include <stdio.h>
#include <stdlib.h>
#include "tile.c"

/* deprecated: tiles now have stacks */
int main(void){
    Tile *t = newTile();
    printTile(t);
    Tile *n;
    n = walk(t,0);
    n->data = 5;
    printTile(n);
    n = walk(n, 0);
    printTile(n);
    n = walk(n,3);
    printTile(n);
    free(n);
    free(t);
}
