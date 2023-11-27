#include "lists.h"
/**
 * check_cycle - checks cyle
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *faster, *slower;
	if (!list || !list->next)
		return(0);
	faster = list->next->next;
	slower = list;

	while (slower != NULL && faster != NULL && faster->next != NULL)
	{
		slower = slower->next;
		faster = faster->next->next;

		if (slower == faster)
			return (1);
	}
	return (0);
}

