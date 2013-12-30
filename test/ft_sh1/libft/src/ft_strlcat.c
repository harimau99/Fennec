/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 10:56:36 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:25 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	char	*save;
	size_t	length;
	size_t	total_length;

	save = dst;
	length = 0;
	total_length = ft_strlen(src) + ft_strlen(dst);
	while (length < size && *dst)
	{
		dst++;
		length++;
	}
	if (size <= length)
		return (size + ft_strlen(src));
	while (length < (size - 1) && *src)
	{
		*dst++ = *src++;
		length++;
	}
	*dst = '\0';
	return (total_length);
}

