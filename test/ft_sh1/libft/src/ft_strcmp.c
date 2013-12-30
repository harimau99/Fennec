/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/20 13:02:40 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:52:17 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_strcmp(const char *s1, const char *s2)
{
	while (*s1)
	{
		if (*s2 == '\0')
			return (1);
		if (*(unsigned char *)s2 > *(unsigned char *)s1)
			return (-1);
		if (*(unsigned char *)s1 > *(unsigned char *)s2)
			return (1);
		s1++;
		s2++;
	}
	if (*s2)
		return (-1);
	return (0);
}

