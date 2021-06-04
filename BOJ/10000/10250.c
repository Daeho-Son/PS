#include <stdio.h>

void	get_room_number()
{
	int		T;
	int		H, W, N;

	scanf("%d", &T);
	while(T--)
	{
		scanf("%d %d %d", &H, &W, &N);
		if (N % H == 0)
			printf("%d\n", H * 100 + (N / H));
		else
			printf("%d\n", (N % H) * 100 + (N / H) + 1);
	}
}

int		main(void)
{
	get_room_number();
	return (0);
}
