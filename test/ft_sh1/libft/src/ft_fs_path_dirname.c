/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fs_path_dirname.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/04 22:17:57 by ksever            #+#    #+#             */
/*   Updated: 2013/12/09 01:52:55 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_fs_path_dirname(const char *path)
{
	char	*last_slash;
	char	*subpath;
	char	*final;

	if ((last_slash = ft_strrchr(path, '/')) == NULL)
		return (ft_strdup(path));
	if (ft_strlen(last_slash) == 1 && ft_strlen(path) > 1)
	{
		subpath = ft_strsub(path, 0, ft_strlen(path) - 1);
		last_slash = ft_strrchr(subpath, '/');
		if (last_slash == NULL)
		{
			final = ft_strsub(path, 0, ft_strlen(path) - 1);
			free(subpath);
			return (final);
		}
		else
		{
			final = ft_strsub(last_slash + 1, 0, ft_strlen(last_slash) - 1);
			free(subpath);
			return (final);
		}
	}
	return (ft_strsub(last_slash + 1, 0, ft_strlen(last_slash)));
}

