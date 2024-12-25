#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
   struct node *next;
}
node;

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        printf("Error\n");
    }
    
    node *list = NULL;
    for (int i = 1; i < argc; i++)
    {
         int number2 = atoi(argv[i]);
        node *n = malloc(sizeof(node));
        n->number = number2;
        n->next = NULL;

       
        if (list == NULL)
        {
            list = n;
        }
       else 
       {
            node *ptr;
        for (ptr = list; ptr->next != NULL; ptr = ptr->next)
        {
           
        }
         ptr->next = n;
        }
    }
    
    for (node *ptr = list;  ptr->next != NULL ; ptr = ptr->next)
    {
        printf("%i, ", ptr->number);
    }
    
      while (list != NULL)
    {
        node *tmp = list;
        list = list->next;
        free(tmp);
    }

}
