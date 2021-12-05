#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct s_node
{
	int				data;
	struct s_node	*next;
}					t_node;

typedef struct s_set
{
	struct s_node	*head;
	struct s_node	*tail;
	int				count;
}					t_set;

t_node	*create(int data)
{
	t_node	*new_node;

	new_node = (t_node *)malloc(sizeof(t_node));
	if (!new_node)
		return (0);
	new_node->data = data;
	new_node->next = NULL;
	return (new_node);
}

/* test_function */
void	print_set(t_set *set)
{
	printf("# print_set\n");
	t_node *node;

	node = set->head;
	printf("data: ");
	while (node)
	{
		printf("%d  ", node->data);
		node = node->next;
	}
	printf("\n\n");
}

t_set	*init_set(int N)
{
	t_set	*set;
	t_node	*node;
	int	n;

	set = (t_set *)malloc(sizeof(t_set));
	if (!set)
		return (0);
	if (N == 0)
		return (set);
	memset(set, 0, sizeof(t_set));
	n = -1;
	while (++n < N)
	{
		node = create(n + 1);
		if (!node)
			return (0);
		if (!set->head)
		{
			set->head = node;
			set->tail = node;
		}
		else
		{
			if (set->tail)
				set->tail->next = node;
			set->tail = node;
		}
		set->count++;
	}
	return (set);
}

int		main(void)
{
	t_set	*set1;
	t_set	*set2;
	t_set	*set3;
	int		N;
	
	scanf("%d", &N);
	set1 = init_set(N);
	set2 = init_set(0);
	set3 = init_set(0);
	if (!set1)
		return (-1);
	print_set(set1);
	print_set(set2);
	print_set(set3);
	return (0);
}
