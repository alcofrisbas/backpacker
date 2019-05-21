typedef struct StackValue StackValue;

struct StackValue {
    int data;
    StackValue *next;
};

/* mallocs */
StackValue *newStack(){
    StackValue *s = malloc(sizeof(StackValue));
    if (s != NULL ) {
        s->next = NULL;
        s->data = 0;
        return s;
    }
    printf("MEMORY ERROR: STACK CREATION\n");
    exit(1);
}


/* mallocs */
void push(StackValue *head, int new) {
    StackValue *n = newStack();
    StackValue *p;
    p = head->next;
    n->data = new;
    n->next = p;
    head->next = n;
}

/* frees 1
 * FAIL SILENTLY... this is a design decision
 */
int pop(StackValue *head){
    if (head->next == NULL){
        return 0;
    }
    StackValue *p, *c;
    int i;
    c = head->next;
    p = c->next;
    head->next = p;
    i = c->data;
    free(c);
    return i;
}

/* FAIL SILENTLY... this is a design decision */
int peek(StackValue *head) {
    if (head->next != NULL) {
        return head->next->data;
    } return 0;
}

/* frees all */
void freeStack(StackValue *head){
    if (head != NULL){
        StackValue *s = head->next;
        free(head);
        freeStack(s);
    }
}

void printS_(StackValue *s, int newline){
    if (s != NULL){
        printf("%d ", s->data);
        fflush(stdout);
        printS_(s->next, newline);
    } else {
        if (newline){
            printf("\n");
            fflush(stdout);
        }
    }
}

void printStack(StackValue *s, int newline){
    printS_(s->next, newline);
}
