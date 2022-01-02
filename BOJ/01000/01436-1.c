#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static char	*ft_itoa(int n)
{
	char	*s;
	int		len;

	s = NULL;
	len = 1;
	if (n < 0)
	{
		len++;
		n *= -1;
	}
	for (int i = n; i >= 10; i/=10)
		len++;
	s = (char *)calloc(len + 1, sizeof(char));
	while (n > 0)
	{
		s[--len] = n % 10 + '0';
		n /= 10;
	}
	if (len == 1)
		s[0] = '-';
	return (s);
}

void	run(int N)
{
	int		start_number;
	char	*s;
	int		rank;

	start_number = 0;
	rank = 0;
	while (1)
	{
		s = ft_itoa(start_number++);
		for (int i = (int)strlen(s) - 3; i >= 0; i--)
		{
			if (strncmp("666", &s[i], 3) == 0)
			{
				rank++;
				break ;
			}
		}
		if (rank == N)
		{
			printf("%s\n", s);
			free(s);
			return ;
		}
		free(s);
		s = NULL;
	}
}

int	main(void)
{
	int		N;

	scanf("%d", &N);
	run(N);
	return (0);
}
