/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fs_path_join.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/04 22:17:57 by ksever            #+#    #+#             */
/*   Updated: 2013/12/08 18:47:10 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_fs_path_join(const char *prefix, const char *path)
{
	char	*temp_pref;
	char	*res;
	int		size;

	temp_pref = NULL;
	if (ft_fs_path_isvalid(path) && !ft_fs_isdotordotdot(path))
		return (ft_strdup(path));
	if (!ft_fs_path_isvalid(prefix))
		temp_pref = ft_strjoinwithglue(".", prefix, '/');
	else
		temp_pref = ft_strdup(prefix);
	size = ft_strlen(temp_pref);
	if (size > 0 && temp_pref[size - 1] == '/')
		res = ft_strjoin(temp_pref, path);
	else
		res = ft_strjoinwithglue(temp_pref, path, '/');
	free(temp_pref);
	return (res);
}

