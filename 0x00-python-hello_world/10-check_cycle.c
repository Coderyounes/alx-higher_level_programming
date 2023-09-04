#include "lists.h"

/**
 * check_cycle - function to detect loops in linkedlist
 *
 * @list: pointer to linked list
 *
 * Return: 0 if it Good, 1 mean there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *onem, *twom;

	if (!list)
	{
		return (0);
	}

	onem = list;
	twom = list->next;

	while(onem != twom)
	{
		if (twom == NULL || twom->next == NULL)
		{
			return (0);
		}
		onem = onem->next;
		twom = twom->next->next;
	}

	return (1);
}
