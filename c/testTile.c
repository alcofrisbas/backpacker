#include <stdio.h>
#include <stdlib.h>
#include "tile.c"

int main(void) {
    Tile *t, *s ,*n;
    /* test for null */
    
    t = tile();
    s = tile();
    if (t->links[0] == NULL){
        printf("null\n");
    }
    
    t->data = 5;
    s->data = 6;
    
    printf("t: %p, data: %i\n", t, t->data);
    printf("s: %p, data: %i\n", s, s->data);
    
    t->links[0] = s;
    
    
    n = walk(t, 0);
    printf("n: %p, data: %i\n", n, n->data);
    free(t);
    free(s);
    return 0;
}