/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 22:55:45 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:24 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strjoin(const char *s1, const char *s2)
{
	char	*newstr;
	char	*save;
	size_t	total;

	total = ft_strlen(s1) + ft_strlen(s2);
	newstr = (char *)malloc(sizeof(char) * (total + 1));
	if (!newstr)
		return (NULL);
	save = newstr;
	while (*s1)
		*newstr++ = *s1++;
	while (*s2)
		*newstr++ = *s2++;
	*newstr = '\0';
	return (save);
}

