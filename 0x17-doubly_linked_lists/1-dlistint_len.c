#include "lists.h"
/**
 * dlistint_len - number of elements in doubly-linked list
 * @h: pointer to the head 
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t numb_of_elements;

	numb_of_elements = 0;
	while (h)
	{
		h = h->next;
		numb_of_elements = numb_of_elements + 1;
	}
	return (numb_of_elements);
}
