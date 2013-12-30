/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strclen.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 16:04:15 by ksever            #+#    #+#             */
/*   Updated: 2013/12/07 13:03:56 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t		ft_strclen(const char *s, char srch)
{
	size_t		count;

	if (!s)
		return (0);
	count = 0;
	while (*s != srch && *s++)
		count++;
	return (count);
}

