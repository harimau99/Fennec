/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_cd_oldpwd.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 00:53:00 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 00:51:11 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <sys/syslimits.h>
#include "libft.h"
#include "ft_shell.h"

int			ft_cmd_cd_oldpwd(void)
{
	char	*cwd;
	char	*oldpwd;

	if (ft_cmd_env_srch("OLDPWD") == -1)
		return (ft_sh_error("42sh: cd: No OLDPWD to move to."));
	cwd = getcwd(NULL, PATH_MAX + 1);
	oldpwd = ft_strdup(ft_cmd_env_get("OLDPWD"));
	if (chdir(oldpwd) == -1)
		return (ft_sh_perror("42sh: cd"));
	ft_cmd_env_set("OLDPWD", cwd);
	ft_cmd_env_set("PWD", oldpwd);
	ft_putendl(oldpwd);
	free(cwd);
	free(oldpwd);
	return (1);
}
