/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 15:45:59 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:37 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *s1, const char *s2, size_t n)
{
	int		i;

	if (ft_strlen(s2) == 0)
		return ((char *)s1);
	i = 0;
	while (s1[i] && ((ft_strlen(s2) + i - 1) < n))
	{
		if (s1[i] == *s2)
		{
			if (ft_strncmp(&s1[i], s2, ft_strlen(s2)) == 0)
				return ((char *)&s1[i]);
		}
		i++;
	}
	return (NULL);
}

