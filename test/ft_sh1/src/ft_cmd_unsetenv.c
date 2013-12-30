/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_unsetenv.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 03:26:37 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 01:16:06 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

static int		ft_cmd_env_dropone(size_t to_remove)
{
	size_t		length;
	char		**newenv;
	size_t		i;
	size_t		j;

	length = ft_sh_tablen(g_shenv);
	if (!(newenv = (char **)malloc(sizeof(char *) * length)))
		return (ft_sh_perror("42sh: malloc:"));
	newenv[length - 1] = NULL;
	i = 0;
	j = 0;
	while (i < length && j < (length - 1))
	{
		if (i == to_remove)
			free(g_shenv[i++]);
		else
			newenv[j++] = g_shenv[i++];
	}
	free(g_shenv);
	g_shenv = newenv;
	return (1);
}

int				ft_cmd_unsetenv(char **argv)
{
	size_t		argv_len;
	int			foundid;
	size_t		i;

	argv_len = ft_sh_tablen(argv);
	if (argv_len < 2)
		return (ft_sh_error("42sh: unsetenv: Too few arguments."));
	i = 1;
	while (i < argv_len)
	{
		if ((foundid = ft_cmd_env_srch(argv[i])) != -1)
			ft_cmd_env_dropone(foundid);
		i++;
	}
	return (1);
}
