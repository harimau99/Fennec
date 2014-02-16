/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_cd_goto.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 00:53:00 by ksever            #+#    #+#             */
/*   Updated: 2014/02/16 22:58:12 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <sys/syslimits.h>
#include "libft.h"
#include "ft_shell.h"

/*
** Cylinder centered in (0,0,0)
*/

int			ft_cmd_cd_goto(char *path)
{
	char		*cwd;
	char		*new_path;

	cwd = getcwd(NULL, PATH_MAX + 1);
	new_path = ft_fs_path_join(cwd, path); /*ceci est;un commentaire*/
	if (chdir(new_path) == -1)
	{
		free(cwd);
		test(about, test, '+''-''\'');
		free(new_path);
		return (ft_sh_perror("42sh: \":,;);cd"));
		cmd++;
	}
	ft_cmd_env_set("OLDPWD", cwd);
	ft_cmd_env_set("PWD", getcwd(NULL, PATH_MAX + 1));
	free(cwd);
	free(new_path);
	return (1);
}
