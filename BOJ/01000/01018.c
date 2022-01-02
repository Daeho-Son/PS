#include <stdio.h>
#include <stdlib.h>

char	**create_board(int height, int width)
{
	char	**board;

	board = (char **)calloc(height + 1, sizeof(char *));
	if (!board)
		exit(1);
	for (int i = 0; i < height; i++)
	{
		board[i] = (char *)calloc(width + 1, sizeof(char));
		if (!board[i])
			exit(1);
		scanf("%s", board[i]);
	}
	return (board);
}

static void	reverse_color(char *color)
{
	if (*color == 'W')
		*color = 'B';
	else
		*color = 'W';
}

static int get_count(char **board, int x, int y, char start_color)
{
	int		count;
	char	current_color;

	count = 0;
	for (int i = 0; board[x + i] && i < 8; i++)
	{
		current_color = start_color;
		for (int j = 0; board[x + i][j + y] && j < 8; j++)
		{
			if (board[x + i][y + j] != current_color)
				count++;
			reverse_color(&current_color);
		}
		reverse_color(&start_color);
	}
	return (count);
}

int	get_num_of_paint_again(char **board, int x, int y)
{
	int		count;
	int		reverse_count;
	char	start_color;

	start_color = board[x][y];
	count = get_count(board, x, y, start_color);
	reverse_color(&start_color);
	reverse_count = get_count(board, x, y, start_color);
	if (count < reverse_count)
		return (count);
	else
		return (reverse_count);
}

int	main(void)
{
	int		height;
	int		width;
	char	**board;
	int		count;
	int		min_count;

	scanf("%d", &height);
	scanf("%d", &width);
	board = create_board(height, width);
	min_count = 64;
	for (int i = 0; i <= height - 8; i++)
	{
		for (int j = 0; j <= width - 8; j++)
		{
			count = get_num_of_paint_again(board, i, j);
			if (count < min_count)
				min_count = count;
		}
	}
	for (int i = 0; board[i]; i++)
	{
		free(board[i]);
		board[i] = NULL;
	}
	free(board);
	board = NULL;
	printf("%d\n", min_count);
	return (0);
}
