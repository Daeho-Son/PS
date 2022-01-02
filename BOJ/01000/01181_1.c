#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_str_data
{
	char 				*str;
	struct s_str_data	*next;
}	t_str_data;

typedef struct s_str_set
{
	struct s_str_data	*start_str_data;
}	t_str_set;

t_str_data	*create_new_str_data(char *str)
{
	t_str_data	*new_str_data;

	new_str_data = (t_str_data *)calloc(1, sizeof(t_str_data));
	if (!new_str_data)
		exit(1);
	new_str_data->str = strdup(str);
	new_str_data->next = NULL;
	return (new_str_data);
}

void	lstadd_sort(t_str_set *str_set, t_str_data *new_str_data)
{
	t_str_data	*str_data;
	t_str_data	*next_str_data;
	char		*tmp_str;

	str_data = str_set->start_str_data;
	while (str_data)
	{
		if (strcmp(str_data->str, new_str_data->str) == 0)
		{
			free(new_str_data->str);
			free(new_str_data);
			break;
		}
		else if (strcmp(str_data->str, new_str_data->str) > 0)
		{
			next_str_data = str_data->next;
			str_data->next = new_str_data;
			new_str_data->next = next_str_data;
			tmp_str = new_str_data->str;
			new_str_data->str = str_data->str;
			str_data->str = tmp_str;
			break;
		}
		else
		{
			if (str_data->next == NULL)
			{
				str_data->next = new_str_data;
				new_str_data->prev = str_data;
				break;
			}
			str_data = str_data->next;
		}
	}
}

void	print_free_str_set(t_str_set *str_set)
{
	t_str_data	*str_data;
	t_str_data	*next_str_data;

	for (int i = 0; i < 51; i++)
	{
		str_data = str_set[i].start_str_data;
		while (str_data)
		{
			printf("%s\n", str_data->str);
			next_str_data = str_data->next;
			free(str_data->str);
			free(str_data);
			str_data = next_str_data;
		}
	}
	free(str_set);
}

int	main(void)
{
	int			num_of_str;
	t_str_set	*str_set;
	char		str[51];
	int			len;

	scanf("%d", &num_of_str);
	str_set = (t_str_set *)calloc(51, sizeof(t_str_set));
	memset(str_set, 0, sizeof(t_str_set) * 51);
	if (!str_set)
		exit(1);
	for (int i = 0; i < num_of_str; i++)
	{
		scanf("%s", str);
		len = (int)strlen(str) - 1;
		if (str_set[len].start_str_data == NULL)
			str_set[len].start_str_data = create_new_str_data(str);
		else
			lstadd_sort(&str_set[len], create_new_str_data(str));
	}
	print_free_str_set(str_set);
	return (0);
}