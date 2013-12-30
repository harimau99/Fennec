/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/22 00:50:33 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:51:57 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t		count;

	count = 0;
	while (count < n)
	{
		if (*((unsigned char *)s + count) == (unsigned char)c)
			return ((unsigned char *)s + count);
		count++;
	}
	return (NULL);
}

