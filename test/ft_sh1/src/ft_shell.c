/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_shell.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/23 19:19:19 by ksever            #+#    #+#             */
/*   Updated: 2014/01/03 14:50:45 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "ft_shell.h"

pid_t	g_currproc = 0;

int		main(void)
{
	if (!ft_sh_init())
		exit(EXIT_FAILURE);
	if (signal(SIGINT, ft_sh_signal_handler) == SIG_ERR)
		return (!ft_sh_error("42sh: Cannot handle signals."));
	while (1)
		ft_sh_dispatch(ft_sh_prompt());
	return (0);
}
