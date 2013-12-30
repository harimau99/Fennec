/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 13:49:56 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:41 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strstr(const char *s1, const char *s2)
{
	if (ft_strlen(s2) == 0)
		return ((char *)s1);
	while (*s1)
	{
		if (*s1 == *s2)
		{
			if (ft_strncmp(s1, s2, ft_strlen(s2)) == 0)
				return ((char *)s1);
		}
		s1++;
	}
	return (NULL);
}

