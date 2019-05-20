#include <stdio.h>
#include <stdlib.h>
#include "tile.c"

int main(void) {
    Tile *t, *s ,*n, *m;
    /* test for null */

    t = newTile();
    s = newTile();


    t->data = 5;
    s->data = 6;

    printTile(t);
    printTile(s);

    t->links[0] = s;


    n = walk(t, 0);
    if (n->links[0] == NULL){
        printf("null\n");
    } else {
        printf("not null: %p\n", n->links[0]);
    }
    m = walk(n, 0);
    printTile(n);
    printTile(m);
    free(t);
    //free(n);
    return 0;
}
