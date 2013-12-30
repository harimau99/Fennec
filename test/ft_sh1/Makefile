# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ksever <ksever@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2013/12/23 16:34:20 by ksever            #+#    #+#              #
#    Updated: 2013/12/30 01:37:21 by ksever           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_minishell1

CC = gcc

vpath %.c src/

SRC = ft_shell.c
SRC += ft_sh_tablen.c
SRC += ft_sh_error.c
SRC += ft_sh_init.c
SRC += ft_sh_prompt.c
SRC += ft_sh_dispatch.c
SRC += ft_cmd_exit.c
SRC += ft_cmd_env.c
SRC += ft_cmd_env_show.c
SRC += ft_cmd_env_srch.c
SRC += ft_cmd_env_set.c
SRC += ft_cmd_env_get.c
SRC += ft_cmd_env_append.c
SRC += ft_cmd_setenv.c
SRC += ft_cmd_unsetenv.c
SRC += ft_cmd_cd.c
SRC += ft_cmd_cd_home.c
SRC += ft_cmd_cd_oldpwd.c
SRC += ft_cmd_cd_goto.c
SRC += ft_cmd_spawn.c
SRC += ft_sh_signal.c

OBJ = $(patsubst %.c, src/%.o, $(SRC))

CFLAGS = -Wall -Werror -Wextra -pedantic

RM = rm -f

all: $(NAME)

.PHONY: all clean fclean re dev

$(NAME): libft/libft.a startlog $(OBJ) includes/ft_shell.h
	@$(CC) $(CFLAGS) -Iincludes/ -Ilibft/includes/ -Llibft/ -lft -o $@ $(OBJ)
	@echo " Done."

clean:
	@$(MAKE) -C libft/ $@
	@$(RM) $(OBJ)

fclean: clean
	@$(MAKE) -C libft/ $@
	@$(RM) $(NAME)

re: fclean all

src/%.o: %.c
	@echo -n .
	@$(CC) $(CFLAGS) -Iincludes/ -Ilibft/includes/ -c $< -o $@

libft/libft.a:
	@$(MAKE) -C ./libft/

dev: libft/libft.a $(OBJ) includes/ft_shell.h
	clang -g $(CFLAGS) -pedantic  -Iincludes/ -Ilibft/includes/\
		 -L libft/ -lft -o $(NAME) $(OBJ)
	llvm-gcc -g $(CFLAGS) -ansi -pedantic  -Iincludes/ -Ilibft/includes/\
		 -L libft/ -lft -o $(NAME) $(OBJ)

startlog:
	@echo "\nCompiling $(NAME)"
