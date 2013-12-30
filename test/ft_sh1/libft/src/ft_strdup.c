/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 19:15:19 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:20 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strdup(const char *s1)
{
	char	*copy;
	char	*save;

	copy = (char *)malloc(sizeof(char) * (ft_strlen(s1) + 1));
	if (copy == NULL)
		return (NULL);
	save = copy;
	while (*s1)
	{
		*copy = *s1;
		copy++;
		s1++;
	}
	*copy = '\0';
	return (save);
}

