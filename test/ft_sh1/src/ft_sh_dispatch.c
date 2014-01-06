/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sh_dispatch.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 01:40:03 by ksever            #+#    #+#             */
/*   Updated: 2014/01/03 14:50:47 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "ft_shell.h"

static t_fptr			g_fptr[] =
{
	{ "exit", &ft_cmd_exit },
	{ "env", &ft_cmd_env },
	{ "setenv", &ft_cmd_setenv },
	{ "unsetenv", &ft_cmd_unsetenv },
	{ "cd", &ft_cmd_cd }
};

int		ft_sh_dispatch(char *cmd)
{
	char	**cmd_split;
	char	*path;
	int		i;

	if (!(cmd_split = ft_strsplit(cmd, ' ')))
		return (ft_sh_error("42sh: Cannot process command."));
	i = 0;
	while (i < 5 && cmd_split[0] != '\0')
	{
		if (ft_strcmp(cmd_split[0], g_fptr[i].cmd) == 0)
			return (g_fptr[i].fct(cmd_split));
		i++;
	}
	if (!(path = ft_cmd_env_get("PATH")))
		path = "/bin:/usr/bin";
	return (ft_cmd_spawn(cmd_split, path));
}
