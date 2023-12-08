#include "lists.h"
/**
 * print_dlistint -function  prints all the elements of a dlistint_t list
 * @h: a pointer to the head
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t numb_of_nodes;

	numb_of_nodes = 0;
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		numb_of_nodes = numb_of_nodes + 1;
	}
	return (numb_of_nodes);
}
