#include "lists.h"

/**
* rev_list - reverses linked list
* @head: head of a linked list
* Return: returns linked list head
*/
listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *temp;

	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;

		prev = current;
		current = temp;
	}
	return (prev);
}

/**
* is_palindrome - function checks for palindrom
* @head: head of linked list
*
* Return: returns length 1 if palindrom 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev, *temp;
	size_t n = 0;

	rev = rev_list(*head);
	temp = *head;
	if (temp == NULL)
	{
		return (1);
	}
	else
	{
		while (temp->next != NULL && rev->next != NULL)
		{
			if (temp->n != rev->n)
			{
				return (0);
			}
			temp = temp->next;
			rev = rev->next;
			n++;
		}

	}

	return (1);
}
