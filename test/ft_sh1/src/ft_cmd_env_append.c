/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_env_append.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 16:13:37 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 00:52:30 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_env_append(char *key, char *value)
{
	size_t		length;
	char		**newenv;

	length = ft_sh_tablen(g_shenv);
	if (!(newenv = (char **)malloc(sizeof(char *) * (length + 2))))
		return (ft_sh_perror("42sh: malloc"));
	newenv[length + 1] = NULL;
	newenv[length] = ft_strjoinwithglue(key, value, '=');
	while (length--)
		newenv[length] = g_shenv[length];
	free(g_shenv);
	g_shenv = newenv;
	return (1);
}
