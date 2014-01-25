/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sh_prompt.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 00:00:37 by ksever            #+#    #+#             */
/*   Updated: 2014/01/25 12:08:23 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"
#include "ft_shell.h"

char		*ft_sh_prompt(void)
{
	char		*cmd;
	int			res;

	if (ft_cmd_env_get("USER"))
		ft_putstr(ft_cmd_env_get("USER"));
	else
		ft_putstr("42sh-v1.0");
	ft_putstr(" $> ");
	res = ft_get_next_line(0, &cmd);
	if (res == -1)
	{
		ft_sh_perror("42sh: ");
		exit(EXIT_FAILURE);
	}
	else if (res == 0)
		exit(EXIT_SUCCESS);
	return (cmd);
}
