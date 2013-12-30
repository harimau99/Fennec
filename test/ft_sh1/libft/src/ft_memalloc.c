/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/22 16:01:01 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:51:54 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	*ft_memalloc(size_t size)
{
	unsigned char	*mem;

	if (!size)
		return (NULL);
	mem = (unsigned char *)malloc(sizeof(unsigned char) * size);
	if (mem == NULL)
		return (NULL);
	while (size-- > 0)
		*((unsigned char *)mem + size) = 0;
	return (mem);
}

