/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_cd.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 00:41:14 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 00:54:17 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_cd(char **argv)
{
	size_t		len;

	len = ft_sh_tablen(argv);
	if (len == 1)
		return (ft_cmd_cd_home());
	else if (len == 2)
	{
		if (ft_strlen(argv[1]) == 1 && argv[1][0] == '-')
			return (ft_cmd_cd_oldpwd());
		else
			return (ft_cmd_cd_goto(argv[1]));
	}
	else if (len > 2)
		return (ft_sh_error("42sh: cd: Too many arguments."));
	return (0);
}
