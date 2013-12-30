/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/22 01:12:01 by ksever            #+#    #+#             */
/*   Updated: 2013/11/22 01:44:55 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*test1;
	unsigned char	*test2;

	test1 = (unsigned char *)s1;
	test2 = (unsigned char *)s2;
	if (n != 0)
	{
		while (n)
		{
			if (*test1 != *test2)
				return (*test1 - *test2);
			test1++;
			test2++;
			n--;
		}
	}
	return (0);
}

