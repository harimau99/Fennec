# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+       #
#    By: ksever <ksever@student.42.fr>              +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+             #
#    Created: 2013/11/19 13:43:22 by ksever            #+#    #+#              #
#    Updated: 2013/12/26 21:41:45 by ksever           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_ls

CC = gcc

SRC = ft_ls.c
SRC += ft_ls_opts_init.c ft_ls_opts_del.c ft_ls_opts_set.c
SRC += ft_ls_cmd_start.c
SRC += ft_ls_argv_parse.c ft_ls_argv_detect.c ft_ls_argv_opts.c
SRC += ft_ls_argv_files.c ft_ls_argv_dflt_file.c
SRC += ft_ls_node_create.c ft_ls_node_append.c ft_ls_node_read.c
SRC += ft_ls_node_swap.c ft_ls_node_is_dots.c ft_ls_node_path_format.c
SRC += ft_ls_node_previous.c ft_ls_node_del.c ft_ls_node_in_node_lvl.c
SRC += ft_ls_node_dir_read.c	
SRC += ft_ls_node_lvl_count.c ft_ls_node_lvl_process.c ft_ls_node_lvl_read.c
SRC += ft_ls_node_lvl_expand.c ft_ls_node_lvl_del.c ft_ls_node_lvl_calc_total.c
SRC += ft_ls_node_lvl_sort.c ft_ls_node_lvl_sort_reverse.c
SRC += ft_ls_node_lvl_has_errors.c 
SRC += ft_ls_sort_name.c ft_ls_sort_time.c
SRC += ft_ls_disp_node_lvl.c ft_ls_disp_node_lvl_prefix.c
SRC += ft_ls_disp_node.c ft_ls_disp_node_simple.c ft_ls_disp_node_details.c
SRC += ft_ls_disp_node_mode.c ft_ls_disp_node_align.c
SRC += ft_ls_disp_node_mode_type.c ft_ls_disp_node_mode_ltype.c
SRC += ft_ls_disp_node_mode_rights.c ft_ls_disp_node_mode_lrights.c
SRC += ft_ls_disp_node_hlinks.c ft_ls_disp_node_size.c
SRC += ft_ls_disp_node_owner_name.c ft_ls_disp_node_group_name.c
SRC += ft_ls_disp_node_mtime.c
SRC += ft_ls_disp_node_willdisp.c ft_ls_node_read_dispcalc.c
SRC += ft_ls_disp_error_usage.c ft_ls_disp_error.c ft_ls_disp_perror.c
SRC += ft_ls_disp_strerror.c

OBJ = $(SRC:.c=.o) 

CFLAGS = -Wall -Werror -Wextra -pedantic
OFLAGS = -O3

RM = rm -vf
	

all: $(NAME)

.PHONY: all clean fclean re dev

$(NAME): libft/libft.a $(OBJ) ft_ls.h
	$(CC) $(CFLAGS) $(OFLAGS) -I libft/includes/ -L libft/ -lft -o $@ $(OBJ)

clean:
	@($(MAKE) -C libft/ $@)
	$(RM) -f $(OBJ)

fclean: clean
	@($(MAKE) -C libft/ $@)
	$(RM) -f $(NAME)

re: fclean all

%.o: %.c
	$(CC) $(CFLAGS) $(OFLAGS) -I libft/includes/ -c $< -o $@

libft/libft.a:
	$(MAKE) -C ./libft/

dev: libft/libft.a $(OBJ) ft_ls.h
	llvm-gcc -g $(CFLAGS) -ansi -pedantic $(OFLAGS) -I libft/includes/\
		 -L libft/ -lft -o $(NAME) $(OBJ)


