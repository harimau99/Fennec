/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_env_get.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <marvin@42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 16:13:37 by ksever            #+#    #+#             */
/*   Updated: 2014/02/18 17:58:16 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

char		*ft_cmd_env_get(char *key)
{
	int			iddata;
	char		*row;
	char		*value;

	if ((iddata = ft_cmd_env_srch(key)) == -1)
		return (NULL);
	row = g_shenv[iddata];
	value = ft_strchr(row, '=') + 1;
	return (value);
}
