#include <stdlib.h>
#include <stdio.h>


struct LinkNode {
    int n;
    struct LinkNode * next;
};
struct LinkNode *createNode(int n);

int main(void)
{
    struct LinkNode *node1 = createNode(1);
    struct LinkNode *node2 = createNode(2);
    struct LinkNode *node3 = createNode(3);
    printf("%p || %p || %pi\n", node1, node2, node3);

    //now that we have the addresses of each node created we can then link them
    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;

    //now that we have linked them lets then print them
    struct LinkNode *currentNode = node1;
    while(currentNode != NULL)
    {
        printf("%d", currentNode->n);
        currentNode = currentNode->next;
    }
    printf("\n");
}
struct LinkNode *createNode(int n)
{
    struct LinkNode *node = malloc(sizeof(struct LinkNode));
    if (node == NULL){
        return NULL;
    }
    node->n = n;
    return node;
}
