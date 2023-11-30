#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 *
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *quick, *slow;

	if (!list || !list->next)
		return (0);

	slow = list;
	quick = list->next;
	while (quick && slow && quick->next)
	{
		if (quick == slow)
			return (1);
		quick = quick->next->next;
		slow = slow->next;
	}
	return (0);
}
