typedef struct Tile Tile;
/*
0: north
1: west
2: east
3: south
*/
struct Tile{
    int x, y;
    struct Tile* links[4];
    int data;
};

Tile* tile(void){
    Tile *t = malloc(sizeof(Tile));
    return t;
}

Tile* walk(Tile *t, int dir) {
    Tile* next;
    if (t->links[dir] != NULL) {
        //printf("found\n");
        //fflush(stdout);
        //printf("%d\n",t->links[dir]->data);
        next = t->links[dir];
        //printf("");
    }else {
        next = tile();
        printf("not found\n");
    }
    return next;
}