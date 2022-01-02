CC			= gcc
CFLAGS		= -Wall -Wextra -Werror -g -fsanitize=address

NAME		= boj
NUMBER		= 07568
SRCS		= $(NUMBER).c
OBJS		= $(SRCS:.c=.o)

%.o		: %.c
	$(CC) $(CFLAGS) -c $< -o $@

all 	: $(NAME)

$(NAME)	: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -lm -o $(NAME)

test	: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -lm -o $(NAME)
	./make_test.sh

clean 	:
	rm -f $(OBJS)

fclean 	:
	rm -f $(NAME)

re		: fclean all

.PHONY	: all clean fclean re
