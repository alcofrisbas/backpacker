#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>



void parseEval(Tile *tknList){
    int x = 0;
    Tile *n = tknList;
    Tile *o = newTile();
    Tile *p = o;
    StackValue *s = newStack();
    while ( n->links[0] != NULL) {
        //printf("%d\n", peek(n->head));
        if(peek(n->head) == 0){
            pop(n->head);
            printf("Keyword: %c\n", peek(n->head));
            char value = (char) peek(n->head);
            if (value == 'w'){
                p = walk(p, 0);
            }if (value == 's'){
                p = walk(p, 3);
            }if (value == 'a'){
                p = walk(p, 1);
            }if (value == 'd'){
                p = walk(p, 2);
            }
            push(n->head, 0);

        } else if (peek(n->head) == 1){
            pop(n->head);
            printf("Symbol:  %c\n", peek(n->head));
            push(n->head, 1);
        } else if (peek(n->head) == 2) {
            pop(n->head);
            printf("Number:  %d\n", peek(n->head));
            push(n->head, 2);
        }
        n = n->links[0];
        x += 1;
    }
    tileFree(o);
    freeStack(s);
}
