#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "stack.c"
#include "tile.c"
#include "tokenize.c"

/*
 * Tokenizing test...
 */

int main(int argc, char **argv){
    Tile *t, *n;
    t = tokenize(t, argv[1]);
    n = t;
    while ( n->links[0] != NULL) {
        printTile(n);
        n = n->links[0];
    }
    tileFree(t);
    return 0;
}