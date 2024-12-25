#include <stdio.h>
#include <stdlib.h>

 typedef struct node
{
    int number;
    node *next;
}
node;

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Error\n");
        return 1;
    }
    
    node *list = NULL;
    for (int i = 1; i < argc; i++)
    {
        node *n = malloc(sizeof(node));     
        int number2 = atoi(argv[i]);
        n->number = number2;
        n->next = NULL;
        if (list == NULL)
        {
            list = n;
        }
        else
        {
            for (node *ptr = list; ptr->next != NULL ; ptr = ptr->next)
            {
                ptr->next = n;
            }
            
        }
          
    }
    
    




}
