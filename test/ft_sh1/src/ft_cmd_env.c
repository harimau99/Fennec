/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cmd_env.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 03:26:37 by ksever            #+#    #+#             */
/*   Updated: 2013/12/27 03:54:37 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "ft_shell.h"

int		ft_cmd_env(char **argv)
{
	size_t		i;

	(void)argv;
	i = 0;
	while (g_shenv[i])
	{
		ft_putendl(g_shenv[i]);
		i++;
	}
	return (1);
}
