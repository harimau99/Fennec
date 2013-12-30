/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 21:14:01 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:00 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *s1, const void *s2, size_t n)
{
	size_t	idx;

	idx = 0;
	while (idx < n)
	{
		*((unsigned char *)s1 + idx) = *((unsigned char *)s2 + idx);
		idx++;
	}
	return (s1);
}

