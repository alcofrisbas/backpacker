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
        next = t->links[dir];
        
    }else {
        /* create the new tile
        later, this will have to be
        pretty smart.
        right now, i need to 
        just get it to work...
        */
        next = tile();
        // for eventual double linkage
        //t->links[3-dir] = next;
        printf("not found\n");
    }
    return next;
}