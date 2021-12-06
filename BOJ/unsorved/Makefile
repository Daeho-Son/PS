CC			= gcc
CFLAGS		= -Wall -Wextra -Werror

NAME		= boj
SRCS		= 11050.c
OBJS		= $(SRCS:.c=.o)

%.o		: %.c
	$(CC) $(CFLAGS) -c $< -o $@

all 	: $(NAME)

$(NAME)	: $(OBJS)
	$(CC) $(OBJS) -o $(NAME)

test	: $(OBJS)
	$(CC) $(OBJS) -o $(NAME)

clean 	:
	rm -f $(OBJS)

fclean 	:
	rm -f $(NAME)

re		: fclean all

.PHONY	: all clean fclean re
