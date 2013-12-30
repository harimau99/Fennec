/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sh_signal.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/28 21:29:12 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 01:16:49 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <signal.h>
#include "libft.h"
#include "ft_shell.h"

void		ft_sh_signal_handler(int sigid)
{
	int			res;

	if (sigid == SIGINT && g_currproc != 0)
	{
		res = kill(g_currproc, sigid);
		if (res == 0)
			g_currproc = 0;
	}
	ft_putstr("\n");
}
