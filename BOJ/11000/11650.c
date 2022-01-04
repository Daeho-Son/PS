#include <stdio.h>
#include <stdlib.h>

int		sorted_coord_x[200001] = { 0, };
int		sorted_coord_y[200001] = { 0, };

typedef struct s_coord
{
	int		*coord_x;
	int		*coord_y;
}	t_coord;

static void	sort_coord_l(t_coord *coord, int *s_i, int *l_i)
{
	sorted_coord_x[*s_i] = coord->coord_x[*l_i];
	sorted_coord_y[*s_i] = coord->coord_y[*l_i];
	(*s_i)++;
	(*l_i)++;
}

static void sort_coord_r(t_coord *coord, int *s_i, int *r_i)
{
	sorted_coord_x[*s_i] = coord->coord_x[*r_i];
	sorted_coord_y[*s_i] = coord->coord_y[*r_i];
	(*s_i)++;
	(*r_i)++;
}

static void	combine(t_coord *coord, int left, int mid, int right)
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
			sort_coord_l(coord, &s_i, &l_i);
		else if (l_i > mid && r_i <= right)
			sort_coord_r(coord, &s_i, &r_i);
		else if (coord->coord_x[l_i] == coord->coord_x[r_i] && \
			coord->coord_y[l_i] <= coord->coord_y[r_i])
			sort_coord_l(coord, &s_i, &l_i);
		else if (coord->coord_x[l_i] == coord->coord_x[r_i] && \
			coord->coord_y[l_i] > coord->coord_y[r_i])
			sort_coord_r(coord, &s_i, &r_i);
		else if (coord->coord_x[l_i] < coord->coord_x[r_i])
			sort_coord_l(coord, &s_i, &l_i);
		else if (coord->coord_x[l_i] > coord->coord_x[r_i])
			sort_coord_r(coord, &s_i, &r_i);
	}
	s_i = 0;
	for (int i = left; i <= right; i++)
	{
		coord->coord_x[i] = sorted_coord_x[s_i];
		coord->coord_y[i] = sorted_coord_y[s_i++];
	}
}

static void	divide(t_coord *coord, int left, int mid, int right)
{
	if (left < right)
	{
		divide(coord, left, (left + mid) / 2, mid);
		divide(coord, mid + 1, (mid + 1 + right) / 2, right);
		combine(coord, left, mid, right);
	}
}

void	ft_sort(t_coord *coord, int num_of_coord)
{
	divide(coord, 0, (num_of_coord - 1) / 2, num_of_coord - 1);
}

int	main(void)
{
	int		num_of_coord;
	t_coord	coord;	

	scanf("%d", &num_of_coord);
	coord.coord_x = (int *)malloc(sizeof(int) * num_of_coord);
	coord.coord_y = (int *)malloc(sizeof(int) * num_of_coord);
	for (int i = 0; i < num_of_coord; i++)
		scanf("%d %d", &coord.coord_x[i], &coord.coord_y[i]);
	ft_sort(&coord, num_of_coord);
	for (int i = 0; i < num_of_coord; i++)
		printf("%d %d\n", coord.coord_x[i], coord.coord_y[i]);
	free(coord.coord_x);
	free(coord.coord_y);
	return (0);
}
