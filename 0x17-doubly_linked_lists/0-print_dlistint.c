#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_dlistint - print a doubly linked list
 * @h: Head
 * Return: Number of elements
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count;

	for (count = 0; h != NULL; h = h->next, count++)
	{
		printf("%d\n", h->n);
	}
	return (count);
}
