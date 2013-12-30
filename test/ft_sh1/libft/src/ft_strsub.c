/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsub.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 22:30:10 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:42 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strsub(const char *s, unsigned int start, size_t len)
{
	char	*new;
	int		i;

	if (!s)
		return (NULL);
	new = (char *)malloc(sizeof(char) * (len + 1));
	if (!new)
		return (NULL);
	i = 0;
	while (s[start] && len-- > 0)
		new[i++] = s[start++];
	new[i] = '\0';
	return (new);
}

