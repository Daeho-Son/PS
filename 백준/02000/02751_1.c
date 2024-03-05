#include <stdio.h>
#include <stdlib.h>

int	sorted[1000000] = { 0, };

void	print_ns(int *ns, int count)
{
	for (int i = 0; i < count; i++)
		printf("%d\n", ns[i]);
}

static void	combine(int *ns, int left, int mid, int right)
{
	int		l_i;
	int		r_i;
	int		s_i;

	l_i = left;
	r_i = mid + 1;
	s_i = 0;
	while (l_i <= mid || r_i <= right)
	{
		if (l_i <= mid && r_i > right)
			sorted[s_i++] = ns[l_i++];
		else if (l_i > mid && r_i <= right)
			sorted[s_i++] = ns[r_i++];
		else if (ns[l_i] <= ns[r_i])
			sorted[s_i++] = ns[l_i++];
		else if (ns[l_i] > ns[r_i])
			sorted[s_i++] = ns[r_i++];
	}
	s_i = 0;
	for (int i = left; i <= right; i++)
	{
		ns[i] = sorted[s_i];
		sorted[s_i++] = 0;
	}
}

static void	divide(int *ns, int left, int mid, int right)
{
	if (left < right)
	{
		divide(ns, left, (left + mid) / 2, mid);
		divide(ns, mid + 1, (mid + 1 + right) / 2, right);
		combine(ns, left, mid, right);
	}
}

void	ft_quick_sort(int *ns, int count)
{
	divide(ns, 0, (count - 1) / 2, count - 1);
}

int	main(void)
{
	int		count;
	int		*ns;

	scanf("%d", &count);
	ns = (int *)malloc(sizeof(int) * count);
	for (int i = 0; i < count; i++)
		scanf("%d", &ns[i]);
	ft_quick_sort(ns, count);
	print_ns(ns, count);
	free(ns);
	return (0);
}
