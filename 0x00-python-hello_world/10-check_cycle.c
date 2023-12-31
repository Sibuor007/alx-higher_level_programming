#include "lists.h"

/**
 *check_cycle - function that checks for a cycle in a linked list
 *list: pointer to the linked list in question
 *Return: 0 on success, 1 on failure
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list
	listint_t *fast = list

	if(!list)
		return(0);
	while (slow && fast && fast->next)
	{
		slow = slow->next
		fast = fast->next->next
		if (slow == fast)
			return (1);
	}
	return (0);
}
