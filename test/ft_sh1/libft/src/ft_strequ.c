/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strequ.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 21:57:31 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:21 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_bool		ft_strequ(const char *s1, const char *s2)
{
	while (*s1)
	{
		if (*s2 == '\0')
			return (false);
		if (*s2 > *s1)
			return (false);
		if (*s1 > *s2)
			return (false);
		s1++;
		s2++;
	}
	if (*s2)
		return (false);
	return (true);
}

