#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks for palindrome
 * @head: pointer pointing to start of list
 * Return: 1
 */

int is_palindrome(listint_t **head)
{
	int size;
	int options[1028];
	int i;

	size = 0;
	if (head == NULL || *head == NULL)
		return (1);

	while (*head != NULL)
	{
		size++;
		options[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (options[i] != options[size - i - 1])
			return (0);
	}

	return (1);
}
