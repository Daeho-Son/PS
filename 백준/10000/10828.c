#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct s_node
{
	int n;
	struct s_node *next;
} t_node;

void	free_all(t_node **node)
{
	t_node *tmp;

	if (!*node)
		return ;
	while (*node)
	{
		tmp = (*node)->next;
		free(*node);
		*node = NULL;
		*node = tmp;
	}
}

void	push(t_node **node, int n)
{
	t_node *new;

	if (!(new = (t_node *)malloc(sizeof(t_node))))
		return ;
	new->n = n;
	new->next = NULL;
	if (!*node)
	{
		*node = new;
		return ;
	}
	new->next = *node;
	*node = new;
}

int		pop(t_node **node)
{
	int		value;
	t_node	*tmp;

	if (!*node)
		return (-1);
	value = (*node)->n;
	tmp = (*node)->next;
	free(*node);
	*node = tmp;
	return (value);
}

int		size(t_node *node)
{
	int		count;

	if (!node)
		return (0);
	count = 1;
	while (node->next)
	{
		count++;
		node = node->next;
	}
	return (count);
}

int		empty(t_node *node)
{
	if (!node)
		return (1);
	return (0);
}

int		top(t_node *node)
{
	if (!node)
		return (-1);
	return (node->n);
}

void	retrieve(t_node **node)
{
	t_node *tmp;

	tmp = *node;
	while (tmp->next)
	{
		printf("%d -> ", tmp->n);
		tmp = tmp-> next;
	}
	printf("%d\n", tmp->n);
}

int		main(void)
{
	int		N;
	char	func[8];
	t_node	*head;
	int		n;
	
	memset(&head, 0, sizeof(t_node));
	scanf("%d", &N);
	while (N--)
	{
		scanf("%s", func);
		if (!strcmp(func, "push"))
		{
			scanf("%d", &n);
			push(&head, n);
		}
		if (!strcmp(func, "pop"))
			printf("%d\n", pop(&head));
		if (!strcmp(func, "size"))
			printf("%d\n", size(head));
		if (!strcmp(func, "empty"))
			printf("%d\n", empty(head));
		if (!strcmp(func, "top"))
			printf("%d\n", top(head));
		if (!strcmp(func, "retrieve"))
			retrieve(&head);
	}
	free_all(&head);
	return (0);
}
