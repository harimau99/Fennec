/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_setenv.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 03:26:37 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 00:48:54 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_setenv(char **argv)
{
	size_t		argv_len;
	char		*value;

	argv_len = ft_sh_tablen(argv);
	if (argv_len > 3)
		return (ft_sh_error("42sh: setenv: Too many arguments."));
	else if (argv_len <= 1)
		return (ft_cmd_env_show());
	value = (argv_len == 3 ? argv[2] : "\0");
	if (ft_strchr(argv[1], '=') != NULL)
		return (ft_sh_error("42sh: setenv: Syntax error."));
	return (ft_cmd_env_set(argv[1], value));
}
