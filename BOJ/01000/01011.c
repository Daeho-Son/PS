#include <stdio.h>

int		main(void)
{
	int			T;		// Tase case
	int	x, y;	// x: Start, y: End. (0 <= x < y < 2^31)
	int	move_count;
	int	remain_space;
	int	move;

	scanf("%d", &T);
	while (T--)
	{
		scanf("%d %d", &x, &y);
		move_count = 0;
		remain_space = y - x;
		move = 1;
		while (remain_space > 0)
		{
			if (remain_space < move)
				move_count -= 1;
			remain_space -= (move * 2);
			move_count += 2;
			if (remain_space <= 0)
			{
				if (remain_space == -(move))
					move_count -= 1;
				break ;
			}
			move++;
		}
		printf("%d\n", move_count);
	}
	return (0);
}
