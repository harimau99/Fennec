/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_env_srch.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 03:26:37 by ksever            #+#    #+#             */
/*   Updated: 2014/01/17 21:41:10 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_env_srch(char *key)
{
	size_t		i;
	char		*srchstr;

	if (!key)
		return (-1);
	srchstr = ft_strjoin(key, "=");
	if (!srchstr)
		return (-1);
	i = 0;
	while (g_shenv[i])
	{
		if (ft_strncmp(g_shenv[i], srchstr, ft_strlen(srchstr)) == 0)
		{
			free(srchstr);
			return (i);
		}
		i++;
	}
	return (-1);
}
