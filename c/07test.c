#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "stack.c"
#include "tile.c"
#include "tokenize.c"
#include "parseEval.c"

/*
 * beginning the parsing/eval testing
 */

int main(int argc, char **argv){
    Tile *t, *n;
    t = tokenize(t, argv[1]);
    parseEval(t);
    tileFree(t);
    return 0;
}