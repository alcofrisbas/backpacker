#include <math.h>
typedef struct Tile Tile;
/*
0: north
1: west
2: east
3: south
*/
struct Tile{
    /*
     * x, y are coords
     * seen: 0 or 1 for search algos
     * created: makes a single path
     * based on a walk for deletion...
     */
    int x, y, seen, created;
    struct Tile* links[4];
    struct Tile* creator;
    int data;
};

Tile* newTile(void){
    Tile *t;
    t  = malloc(sizeof(Tile));
    if (t == NULL ) {
        printf("MEMORY ERROR: TILE\n" );
        exit(1);
    }
    t->x = 0;
    t->y = 0;
    t->seen = 0;
    t->created=0;
    t->links[0] = NULL;
    t->links[1] = NULL;
    t->links[2] = NULL;
    t->links[3] = NULL;
    t->data = 0;
    return t;
}

void connect_adjacent(Tile *t, Tile *s, int dir){
    t->links[dir] = s;
    s->links[3-dir] = t;
    if (!s->created) {
        s->creator = t;
    }
}
/* works */
int connected(Tile *t, Tile *s) {
    int i;
    for (i=0;i<4;i++){
        if (t->links[i] == s || s->links[i] == t) {
            return 1;
        }
    }
    return 0;
}
int adjacent(Tile *t, Tile *s){
    if (abs((t->x+t->y)-(s->x+s->y)) == 1){
        return 1;
    }
    return 0;
}

// int direction(Tile *t, Tile *s){
//     if (t->x > s->x){
//         return 1;
//     }if (t->x < s->x){
//         return 2;
//     }if (t->y > s->y){
//         return 0;
//     }if (t->y < s->y){
//         return 3;
//     }
//     return 0;
// }

int deadEnd(Tile *t){
    int i,j;
    j=0;
    for (i=0;i<4;i++){
        if (t->links[i] != NULL){
            j += 1;
        }
    }
    if (j > 1){
        return 1;
    }
    return 0;
}

void clean(Tile *t){
    if (t != NULL && t->seen){
        t->seen = 0;
        int i;
        for(i=0;i<4;i++){
            clean(t->links[i]);
        }

    }

}
/* for connecting to non-adjacent tiles
this needs to be like bfs*/
void connect(Tile *current, Tile *goal){
    if (current != NULL && ! current->seen) {
        current->seen = 1;
        if (adjacent(current, goal) && !connected(current, goal)) {
            if (current->x > goal->x){
                connect_adjacent(current, goal, 1);
            }if (current->x < goal->x){
                connect_adjacent(current, goal, 2);
            }if (current->y > goal->y){
                connect_adjacent(current, goal, 0);
            }if (current->y < goal->y){
                connect_adjacent(current, goal, 3);
            }
        } else {
            int i;
            for(i=0;i<4;i++){
                connect(current->links[i], goal);
            }
        }
    }
}

Tile* walk(Tile *t, int dir) {
    Tile* next;
    if (t->links[dir] != NULL) {
        next = t->links[dir];
    } else {
        next = newTile();
        /*
        0 -> 0,1
        1 -> -1, 0
        2 -> 1, 0
        3 -> 0, -1
        */
        if (dir == 0){
            next->y = t->y + 1;
            next->x = t->x;
        } else if (dir == 1){
            next->x = t->x - 1;
            next->y = t->y;
        } else if (dir == 2){
            next->x = t->x + 1;
            next->y = t->y;
        } else if (dir == 3){
            next->y = t->y - 1;
            next->x = t->x;
        }
        connect_adjacent(t, next, dir);
        connect(next, next);
        clean(next);
    }
    return next;
}

void printTile(Tile *t);

void tileFree(Tile *t){
    int i;
    for(i=0;i<4;i++){
        if (t->links[i]!= NULL && t->links[i]->creator==t){
            t->links[i]->links[3-i] = NULL;
            tileFree(t->links[i]);
        }
    }
    printf("freeing: ");
    printTile(t);
    free(t);
    t = NULL;
}

void printTile(Tile *t){
    printf("addr: %p coords: (%d, %d)\tdata: %d\tstatus: %d\n", t, t->x, t->y, t->data, t->seen);
}
