#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool	is_ascending(int *s)
{
	int		i;

	i = -1;
	while (++i < 7)
	{
		if (s[i] >= s[i + 1])
			return (false);
	}
	return (true);
}

bool	is_descending(int *s)
{
	int		i;

	i = -1;
	while (++i < 7)
	{
		if (s[i] <= s[i + 1])
			return (false);
	}
	return (true);
}

int	main(void)
{
	int		input[8];

	for (int i = 0; i < 8; i++)
		scanf("%d", &input[i]);
	if (is_ascending(input))
		printf("ascending\n");
	else if (is_descending(input))
		printf("descending\n");
	else
		printf("mixed\n");
	return (0);
}
