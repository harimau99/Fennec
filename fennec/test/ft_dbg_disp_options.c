/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_dbg_disp_options.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/29 18:47:24 by ksever            #+#    #+#             */
/*   Updated: 2013/12/11 01:11:01 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include "ft_ls.h"

void	ft_dbg_disp_options(void)
{
	printf("=+=+=+=+= ft_ls Options =+=+=+=\n");
	printf("Display method (simple: 0, list: 1): %d\n", g_opts->display);
	printf("Display links max len              : %d\n", g_opts->disp_param.nblink_len);
	printf("Display user max len               : %d\n", g_opts->disp_param.user_len);
	printf("Display group max len              : %d\n", g_opts->disp_param.group_len);
	printf("Display size max len               : %d\n", g_opts->disp_param.size_len);
	printf("Sorting method (name: 1, time: 2)  : %d\n", g_opts->sorting);
	printf("Is reversed  : %d\n", g_opts->is_reversed);
	printf("Is recursive : %d\n", g_opts->is_recursive);
	printf("Show hidden  : %d\n", g_opts->show_hidden);
	printf("Drops Opts   : %d\n", g_opts->drop_opts);
	printf("=+=+=+=+= Base File/Dir List =+=+=+=\n");
	ft_dbg_disp_files(g_opts->base_node);
	printf("=+=+=+=+= Base Official output =+=+=+=\n");
	ft_ls_disp_node_lvl(NULL, g_opts->base_node);
	printf("=+=+=+=+= Current File/Dir List =+=+=+=\n");
	ft_dbg_disp_files(g_opts->curr_node);
	printf("=+=+=+=+= Current Official output =+=+=+=\n");
	ft_ls_disp_node_lvl(NULL, g_opts->curr_node);
	printf("=+=+=+=+= End =+=+=+=\n");
}

void	ft_dbg_disp_node_info(t_nlist *lst)
{
	printf("Name: \"%s\"", lst->name);
	printf(" Addr: (%p)", (void *)lst);
	printf("[ERRLVL: %d; Checked: %d; D: %d; Total: %d, N-> %p", lst->errlvl, lst->checked,
			lst->displayed, lst->dir_total, (void *)lst->next);
	printf("; Type: %o", lst->nstat.st_mode);
	printf("]\n");
}

void	ft_dbg_disp_files(t_nlist *lst)
{
	while (lst)
	{
		ft_dbg_disp_node_info(lst);
		if (lst->below != NULL)
		{
			printf("vvvvvvvv Subdir vvvvvvvvv\n");
			ft_dbg_disp_files(lst->below);
			printf("AAAAAAAA END AAAAAAAAA\n");
		}
		lst = lst->next;
	}
}

