/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsplit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/23 23:18:17 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:40 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static int	ft_wdcount(const char *s, char sep)
{
	int		num;
	int		i;

	num = 0;
	i = 0;
	while (s[i])
	{
		while (s[i] && s[i] == sep)
			i++;
		if (s[i] && s[i] != sep)
		{
			num++;
			while (s[i] && s[i] != sep)
				i++;
		}
	}
	return (num);
}

static int	ft_wdlen(const char *s, char sep)
{
	int		len;

	len = 0;
	while (s[len] != sep && s[len])
		len++;
	return (len);
}

static char	*ft_wdncpy(const char *src, char c)
{
	char	*item;
	int		len;

	len = ft_wdlen(src, c);
	item = (char *)malloc(sizeof(char) * (len + 1));
	if (!item)
		return (NULL);
	ft_strncpy(item, src, len);
	item[len] = '\0';
	return (item);
}

char		**ft_strsplit(const char *s, char c)
{
	char	**res;
	int		n[2];

	n[0] = 0;
	n[1] = 0;
	if (!s)
		return (NULL);
	res = (char **)malloc(sizeof(char *) * (ft_wdcount(s, c) + 1));
	if (!res)
		return (NULL);
	while (n[0] < ft_wdcount(s, c))
	{
		while (s[n[1]] == c)
			n[1] = n[1] + 1;
		if ((n[1] == 0 && s[n[1]] != c) || (s[n[1] - 1] == c && s[n[1]] != c))
		{
			res[n[0]] = ft_wdncpy(&s[n[1]], c);
			n[1] += ft_wdlen(&s[n[1]], c);
		}
		n[1] = n[1] + 1;
		n[0] = n[0] + 1;
	}
	res[ft_wdcount(s, c)] = '\0';
	return (res);
}

