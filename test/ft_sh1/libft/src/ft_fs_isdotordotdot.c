/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fs_isdotordotdot.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/04 22:21:11 by ksever            #+#    #+#             */
/*   Updated: 2013/12/05 17:34:11 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_bool		ft_fs_isdotordotdot(const char *str)
{
	if (ft_strlen(str) == 1 && *str == '.')
		return (true);
	else if (ft_strlen(str) == 2 && str[0] == '.' && str[1] == '.')
		return (true);
	return (false);
}

