/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_cd_home.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 00:53:00 by ksever            #+#    #+#             */
/*   Updated: 2014/01/22 13:09:28 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <sys/syslimits.h>
#include "libft.h"
#include "ft_shell.h"

int			ft_cmd_cd_home(void)
{
	int		idhome;
	char	*cwd;

	if ((idhome = ft_cmd_env_srch("HOME")) == -1)
		return (ft_sh_error("42sh: cd: No HOME directory."));
	cwd = getcwd(NULL, PATH_MAX + 1);
	if (chdir(ft_cmd_env_get("HOME")) == -1)
		return (ft_sh_perror("42sh: cd"));
	ft_cmd_env_set("OLDPWD", cwd);
	ft_cmd_env_set("PWD", ft_cmd_env_get("HOME"));
	free(cwd);
	return (1);
}
