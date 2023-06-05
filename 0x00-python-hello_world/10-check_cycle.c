#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: Singly-linked list
 *
 * Return: if no cycle 0, else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *previous, *current;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	previous = list->next;
	current = list->next->next;

	while (previous && current && current->next)
	{
		if (previous == current)
		{
			return (1);
		}
		previous = previous->next;
		current = current->next->next;
	}
	return (0);
}
