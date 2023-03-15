#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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
