/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 16:04:15 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:23:57 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t		ft_strlen(const char *s)
{
	const char		*c;
	const int		*word;
	unsigned int	word_text;

	if (!s)
		return (0);
	word = (int *)s;
	while (1)
	{
		word_text = *word;
		if ((word_text - 0x01010101) & ~word_text & 0x80808080)
		{
			c = (const char *)word;
			while (*c)
				c++;
			return (c - s);
		}
		word++;
	}
}

