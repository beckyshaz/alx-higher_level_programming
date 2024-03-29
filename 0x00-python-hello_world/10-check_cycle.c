#include "lists.h"
/**
 *check_cycle - function that checks if there is a circle in a linked list
 *@list: linked list to be checked
 *Return: 1 if there is a circle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list;
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}
	return (0);
}
