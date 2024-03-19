#include "lists.h"
#include <stdio.h>

listint_t *find_middle_node(listint_t **head);
listint_t *reverse_secondHalf_list(listint_t *head);
int compare_first_second_lists(listint_t *head, listint_t *secondHalf_head);

int is_palindrome(listint_t **head)
{
listint_t *middleNode = find_middle_node(head);
listint_t *new_secondHalf_head = reverse_secondHalf_list(middleNode->next);
return (compare_first_second_lists(*head, new_secondHalf_head));
}

listint_t *find_middle_node(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}
return (slow);
}

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
return (prev);
}
int compare_first_second_lists(listint_t *head, listint_t *secondHalf_head)
{
while (head != NULL && secondHalf_head != NULL)
{
printf("%d %d\n", head->n, secondHalf_head->n);
if (head->n != secondHalf_head->n)
{
return (0);
}
head = head->next;
secondHalf_head = secondHalf_head->next;
}
return (1);
}
