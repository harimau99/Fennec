/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fs_path_isvalid.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/04 22:21:11 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:51:32 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_bool		ft_fs_path_isvalid(const char *path)
{
	t_bool		valid;

	if (!path)
		return (false);
	valid = false;
	if (ft_fs_isdotordotdot(path))
		valid = true;
	else if (*path == '/')
		valid = true;
	else if (ft_strlen(path) >= 2 && path[0] == '.' && path[1] == '/')
		valid = true;
	else if (ft_strlen(path) >= 3 && path[0] == '.' && path[1] == '.'
			&& path[2] == '/')
		valid = true;
	while (*path)
	{
		if (!ft_isprint(*path++))
			valid = false;
	}
	return (valid);
}

