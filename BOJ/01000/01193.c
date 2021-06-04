#include <stdio.h>

int		main(void)
{
	int	n;
	int	flag;	// 0: left, 1: down
	int	x_coord;
	int	y_coord;

	scanf("%d", &n);
	flag = 0;
	x_coord = 1;
	y_coord = 1;
	while (n-- > 1)
	{
		if (flag == 0 && x_coord == 1)
		{
			y_coord += 1;
			flag = 1;
		}
		else if (flag == 1 && (x_coord == 1 || (x_coord != 1 && y_coord != 1)))
		{
			x_coord += 1;
			y_coord -= 1;
		}
		else if (flag == 1 && y_coord == 1)
		{
			x_coord += 1;
			flag = 0;
		}
		else if (flag == 0  && (y_coord == 1 || (x_coord != 1 && y_coord != 1)))
		{
			x_coord -= 1;
			y_coord +=1;
		}
	}
	printf("%d/%d\n", x_coord, y_coord);
	return (0);
}
