#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The value to be inserted.
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *temp;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;
    while (current->next != NULL && current->next->n < number)
        current = current->next;

    temp = current->next;
    current->next = new_node;
    new_node->next = temp;

    return (new_node);
}
