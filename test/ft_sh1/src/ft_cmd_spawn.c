/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_spawn.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 16:54:31 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 17:40:07 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/wait.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

int			ft_cmd_execution(char *path, char **argv, char **env)
{
	struct stat		s_statinfo;
	extern int		errno;
	int				result;

	if (stat(path, &s_statinfo) == 0)
	{
		result = execve(path, argv, env);
		free(path);
		if (result == -1)
			exit(!ft_sh_perror("42sh"));
		return (result);
	}
	else
	{
		if (errno != 2)
			ft_sh_perror("42sh");
	}
	free(path);
	return (-1);
}

int			ft_cmd_spawn(char **argv, char *path)
{
	int			i;
	char		*tmppath;
	char		**paths;
	int			process_status;
	int			res;

	paths = ft_strsplit(path, ':');
	if ((g_currproc = fork()) == 0)
	{
		i = 0;
		while (paths[i])
		{
			tmppath = ft_fs_path_join(paths[i], argv[0]);
			if ((res = ft_cmd_execution(tmppath, argv, g_shenv)) != -1)
				exit(res);
			i++;
		}
		exit(!ft_sh_error("42sh: Command not found."));
	}
	else
		return (wait(&process_status));
}
