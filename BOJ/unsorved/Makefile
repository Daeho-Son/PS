CC			= gcc

NAME		= test
SRCS		= 02920.c
OBJS		= $(SRCS:.c=.o)

%.o		: %.c
	$(CC) -c $< -o $@

all 	: $(NAME)

$(NAME)	: $(OBJS)
	$(CC) $(OBJS) -o $(NAME)

clean 	:
	rm -f $(OBJS)

fclean 	:
	rm -f $(NAME)

re		: fclean all

.PHONY	: all clean fclean re
