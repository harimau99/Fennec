/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_env_set.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 16:13:37 by ksever            #+#    #+#             */
/*   Updated: 2014/01/06 19:17:54 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_env_set(char *key, char *value)
{
	int			iddata;

	if ((iddata = ft_cmd_env_srch(key)) == -1)
		return (ft_cmd_env_append(key, value));
	else
	{
		free(g_shenv[iddata]);
		g_shenv[iddata] = ft_strjoinwithglue(key, value, '=');
	}
	return (1);
}
