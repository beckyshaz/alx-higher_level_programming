#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 *insert_node - function that inserts a num into a sorted singly linked list
 *@head: pointer to the first node
 *@number: number to be inserted in the list
 *Return: pointer to the newlist or null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
		*head = newnode;
	else
	{
		temp = *head;
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = newnode;
	}
	return (newnode);

}
