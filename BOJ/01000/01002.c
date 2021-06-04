#include <stdio.h>
#include <math.h>

int		main(void)
{
	int		T;
	float	x1, y1, r1;
	float	x2, y2, r2;
	float	d;
	float	big_r, small_r;

	scanf("%d", &T);
	while (T--)
	{
		scanf("%f %f %f", &x1, &y1, &r1);
		scanf("%f %f %f", &x2, &y2, &r2);
		d = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
		big_r = (r1 > r2) ? r1 : r2;
		small_r = (r1 < r2) ? r1 : r2;
		if (d == 0 && (r1 == r2))
		{
			printf("-1\n");
			continue;
		}
		if ((big_r - small_r < d) && (d < small_r + big_r))
			printf("2\n");
		else if ((big_r - small_r == d) || (small_r + big_r == d))
			printf("1\n");
		else if ((small_r + big_r < d) || (d < big_r - small_r) || (d == 0 && big_r != small_r))
			printf("0\n");
	}
	return (0);
}
