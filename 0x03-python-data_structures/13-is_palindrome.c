#include "lists.h"
#include <stdio.h>

int is_palindrome(listint_t **head)
{
    // we are receiving the the pointer of the head linked list
    
    //we first have to indee there is a linked list
    if (*head == NULL)
    {
        return 1;
    }
    // find the middle node of the linked list so that we can half it.
    listint_t *find_middle_node()
    {
        listint_t *slow = *head;
        listint_t *fast = *head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    listint_t *middleNode = find_middle_node();
    printf("\n");
    printf("Middle node is: %d\n", middleNode->n);

    // after finding the middle node we have to reverse the second half of the linked list

    listint_t *reverse_secondHalf_list(listint_t *head)
    {
        listint_t *prev = NULL;
        listint_t *temp;
        
        while (head != NULL)
        {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }
    listint_t *new_secondHalf_head = reverse_secondHalf_list(middleNode->next);
    printf("first num of reversed list: %d\n", new_secondHalf_head->n);

    /* after reversing the second list then we iterate through both list
     * i.e firstHalf and secondHalf list simultaneously while comparing
     * there values. if values are not equal return 1 else return 0
     *
     */
    int compare_firstHalf_secondHalf_lists(listint_t *head, listint_t *secondHalf_head)
    {
        while (head != NULL && secondHalf_head != NULL)
        {
            printf("%d %d\n", head->n, secondHalf_head->n);
            if (head->n != secondHalf_head->n)
            {
                return 0;
            }
            head = head->next;
            secondHalf_head = secondHalf_head->next;
        }
        return 1;
    }
    return compare_firstHalf_secondHalf_lists(*head, new_secondHalf_head);
}
