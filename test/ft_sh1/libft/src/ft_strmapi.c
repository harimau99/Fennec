/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 21:49:20 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:29 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(const char *s, char (*f)(unsigned int, char))
{
	char	*new;
	char	*save;
	int		i;

	if (!s)
		return (NULL);
	new = ft_strdup(s);
	if (!new)
		return (NULL);
	i = 0;
	save = new;
	while (*new)
	{
		*new = f(i++, *new);
		new++;
	}
	new = '\0';
	return (save);
}

