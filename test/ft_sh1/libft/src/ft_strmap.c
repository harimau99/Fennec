/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 21:31:15 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:28 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmap(const char *s, char (*f)(char))
{
	char	*new;
	char	*save;

	if (!s)
		return (NULL);
	new = ft_strdup(s);
	if (!new)
		return (NULL);
	save = new;
	while (*new)
	{
		*new = f(*new);
		new++;
	}
	new = '\0';
	return (save);
}

