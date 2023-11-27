#include <stdio.h>
#include "lists.h"

/**
 * check_cycle -  function that checks whether cycle is present is list
 *
 * @list1: linked list to be checked
 *
 * Return: 1 if cycle is present in list, 0 if not
 */

int check_cycle(listint_t *list1)

{
	listint_t *slow = list1;
	listint_t *fast = list1;

	if (!list1)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
