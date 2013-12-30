/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnequ.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 22:01:17 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:35 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_bool		ft_strnequ(const char *s1, const char *s2, size_t n)
{
	while (*s1 && n > 0)
	{
		if (*s2 == '\0')
			return (false);
		if (*s2 > *s1)
			return (false);
		if (*s1 > *s2)
			return (false);
		s1++;
		s2++;
		n--;
	}
	if (*s2 && n > 0)
		return (false);
	return (true);
}

