/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sh_init.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/26 23:58:02 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 00:47:44 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

char			**g_shenv;

int		ft_sh_init(void)
{
	size_t		length;

	length = ft_sh_tablen(environ);
	g_shenv = (char **)malloc(sizeof(char *) * (length + 1));
	if (!g_shenv)
		return (ft_sh_perror("42sh: malloc"));
	g_shenv[length] = NULL;
	while (length--)
		g_shenv[length] = ft_strdup(environ[length]);
	return (1);
}
