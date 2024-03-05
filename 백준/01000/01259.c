#include <stdio.h>
#include <string.h>

int	is_palindrome_number(char *s)
{
	int		start;
	int		end;

	start = 0;
	end = (int)strlen(s) - 1;
	while (start <= end)
	{
		if (s[start++] != s[end--])
			return (0);
	}
	return (1);
}

int	main(void)
{
	char	input[6];

	while (1)
	{
		memset(&input, 0, 6);
		scanf("%s", input);
		if (*input == '0')
			return (0);
		if (is_palindrome_number(input))
			printf("yes\n");
		else
			printf("no\n");
	}
	return (0);
}
