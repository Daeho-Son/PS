#include <stdio.h>
#include <stdlib.h>

int		sorted_age_table[100001] = { 0, };

typedef struct s_tables
{
	int		*age_table;
	char	**name_table;
}	t_tables;

void	free_double_pointer(char ***s)
{
	for (int i = 0; (*s)[i]; i++)
	{
		free((*s)[i]);
		(*s)[i] = NULL;
	}
	free(*s);
	*s = NULL;
}

static void combine(t_tables *tables, int left, int mid, int right)
{
	int		l_i;
	int		r_i;
	int		s_i;
	char	**sorted_name_table;

	sorted_name_table = (char **)calloc(right - left + 2, sizeof(char *));
	l_i = left;
	r_i = mid + 1;
	s_i = 0;
	while (l_i <= mid || r_i <= right)
	{
		if (l_i <= mid && r_i > right)
		{
			sorted_age_table[s_i] = tables->age_table[l_i];
			sorted_name_table[s_i++] = tables->name_table[l_i++];
		}
		else if (l_i > mid && r_i <= right)
		{
			sorted_age_table[s_i] = tables->age_table[r_i];
			sorted_name_table[s_i++] = tables->name_table[r_i++];
		}
		else if (tables->age_table[l_i] <= tables->age_table[r_i])
		{
			sorted_age_table[s_i] = tables->age_table[l_i];
			sorted_name_table[s_i++] = tables->name_table[l_i++];
		}
		else if (tables->age_table[l_i] > tables->age_table[r_i])
		{
			sorted_age_table[s_i] = tables->age_table[r_i];
			sorted_name_table[s_i++] = tables->name_table[r_i++];
		}
	}
	s_i = 0;
	for (int i = left; i <= right; i++)
	{
		tables->age_table[i] = sorted_age_table[s_i];
		tables->name_table[i] = sorted_name_table[s_i++];
	}
	free(sorted_name_table);
}

static void divide(t_tables *tables, int left, int mid, int right)
{
	if (left < right)
	{
		divide(tables, left, (left + mid) / 2, mid);
		divide(tables, mid + 1, (mid + 1 + right) / 2, right);
		combine(tables, left, mid, right);
	}
}

void	ft_sort(t_tables *tables, int num_of_members)
{

	divide(tables, 0, (num_of_members - 1) / 2, num_of_members - 1);
}

int	main(void)
{
	int			num_of_members;
	int			*age_table;
	char		**name_table;
	t_tables	tables;

	scanf("%d", &num_of_members);
	age_table = (int *)malloc(sizeof(int) * num_of_members);
	name_table = (char **)calloc(num_of_members + 1, sizeof(char *));
	tables.age_table = age_table;
	tables.name_table = name_table;
	for (int i = 0; i < num_of_members; i++)
	{
		name_table[i] = (char *)calloc(101, sizeof(char));
		scanf("%d %s", &age_table[i], name_table[i]);
	}
	ft_sort(&tables, num_of_members);
	for (int i = 0; i < num_of_members; i++)
	{
		printf("%d %s\n", age_table[i], name_table[i]);
	}
	free(age_table);
	free_double_pointer(&name_table);
	return (0);
}
