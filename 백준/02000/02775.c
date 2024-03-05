#include <stdio.h>
#include <stdlib.h>

void	get_sum(int **ns, int n)
{
	int	n_index;

	n_index = 1;
	while (n_index < n)
	{
		(*ns)[n_index] = (*ns)[n_index] + (*ns)[n_index - 1];
		n_index++;
	}
}

int		get_number_of_people(int k, int n)
{
	int	result;
	int	*ns;
	int	n_index;
	int	k_index;

	if(!(ns = (int *)malloc(sizeof(int) * n)))
		return (-1);
	n_index = 0;
	while (n_index < n)
	{
		ns[n_index] = n_index + 1;
		n_index++;
	}
	k_index = 1;
	while (k_index <= k)
	{
		get_sum(&ns, n);
		k_index++;
	}
	result = ns[n - 1];
	free(ns);
	ns = NULL;
	return (result);
}

int		main(void)
{
	int		T;	// Test case
	int		k;	// floor
	int		n;	// Unit

	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &k);
		scanf("%d", &n);
		printf("%d\n", get_number_of_people(k, n));
	}
	return (0);
}
