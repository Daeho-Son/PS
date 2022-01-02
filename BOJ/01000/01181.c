#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

static void	combine(char **strs, int left, int mid, int right)
{
	char	**sorted;
	int		s_i;
	int		l_i;
	int		r_i;

	s_i = left;
	l_i = left;
	r_i = mid + 1;
	sorted = (char **)calloc(200001, sizeof(char *));
	while (l_i <= mid || r_i <= right)
	{
		if (l_i <= mid && !(r_i <= right))
		{
			sorted[s_i++] = strs[l_i++];
		}
		else if (!(l_i <= mid) && r_i <= right)
		{
			sorted[s_i++] = strs[r_i++];
		}
		else if (strlen(strs[l_i]) < strlen(strs[r_i]))
		{
			sorted[s_i++] = strs[l_i++];
		}
		else if (strlen(strs[r_i]) < strlen(strs[l_i]))
		{
			sorted[s_i++] = strs[r_i++];
		}
		else if (strcmp(strs[l_i], strs[r_i]) < 0)
		{
			sorted[s_i++] = strs[l_i++];
		}
		else if (strcmp(strs[l_i], strs[r_i]) > 0)
		{
			sorted[s_i++] = strs[r_i++];
		}
		else
		{
			sorted[s_i++] = strs[l_i++];
		}
	}
	s_i = left;
	for (int i = left; i <= right; i++)
	{
		strs[i] = sorted[s_i];
		sorted[s_i] = NULL;
		s_i++;
	}
	free(sorted);
}

static void	divide(char **strs, int left, int mid, int right)
{
	if (left < right)
	{
		divide(strs, left, (left + right) / 2, mid);
		divide(strs, mid + 1, (mid + 1 + right) / 2, right);
		combine(strs, left, mid, right);
	}
}

static void ft_merge_sort(char **strs, int num_of_n)
{
	divide(strs, 0, num_of_n / 2, num_of_n - 1);
}

static void	print_strs(char **s)
{
	for (int i = 0; s[i]; i++)
	{
		if (s[i + 1] && strncmp(s[i], s[i + 1], strlen(s[i + 1])) == 0)
			continue ;
		printf("%s\n", s[i]);
	}
}

int	main(void)
{
	char	**strs;
	int		num_of_n;
	char	str[51];

	scanf("%d", &num_of_n);
	strs = (char **)calloc(num_of_n + 1, sizeof(char *));
	for (int i = 0; i < num_of_n; i++)
	{
		scanf("%s",	str);
		strs[i] = strdup(str);
	}
	ft_merge_sort(strs, num_of_n);
	print_strs(strs);
	free_double_pointer(&strs);
	return (0);
}
