/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/05 00:12:40 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:38 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrev(char *str)
{
	char	*start;
	char	*end;
	char	tmp;

	if (ft_strlen(str) == 0)
		return (str);
	end = str + ft_strlen(str) - 1;
	start = str;
	while (end > start)
	{
		tmp = *start;
		*start++ = *end;
		*end-- = tmp;
	}
	return (str);
}

