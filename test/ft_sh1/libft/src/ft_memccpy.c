/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 21:46:48 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:51:55 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memccpy(void *s1, const void *s2, int c, size_t n)
{
	size_t	count;

	count = 0;
	while (count < n)
	{
		*((unsigned char *)s1 + count) = *((unsigned char *)s2 + count);
		if (*((unsigned char *)s2 + count) == (unsigned char)c)
			return ((unsigned char *)s1 + count + 1);
		count++;
	}
	return (NULL);
}

