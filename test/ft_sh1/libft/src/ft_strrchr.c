/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/21 13:28:20 by ksever            #+#    #+#             */
/*   Updated: 2013/12/09 01:42:38 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		end_count;

	if (c < 0 || c > 127)
		return (NULL);
	end_count = ft_strlen(s);
	while (end_count >= 0)
	{
		if (s[end_count] == (char)c)
			return ((char *)&s[end_count]);
		end_count--;
	}
	return (NULL);
}

