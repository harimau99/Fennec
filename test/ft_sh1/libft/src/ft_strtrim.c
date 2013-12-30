/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 17:24:28 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:42 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strtrim(const char *s)
{
	char	*start;
	char	*end;
	char	*trim;

	if (!s)
		return (NULL);
	while ((*s == ' ' || *s == '\n' || *s == '\t') && *s)
		s++;
	start = (char *)s;
	end = start + ft_strlen(start) - 1;
	while ((*end == ' ' || *end == '\n' || *end == '\t') && end >= start)
		end--;
	if ((end - start) >= 0)
	{
		trim = (char *)malloc(sizeof(char) * (end - start + 1));
		if (!trim)
			return (NULL);
		ft_strncpy(trim, start, end - start + 1);
		trim[end - start + 1] = '\0';
	}
	else
		trim = ft_memalloc(1);
	return (trim);
}

