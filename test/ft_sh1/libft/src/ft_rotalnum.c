/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rotalnum.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/22 21:49:37 by ksever            #+#    #+#             */
/*   Updated: 2014/01/01 23:44:54 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_rotalnum(char *str, int rot_value)
{
	char		*start;

	start = str;
	while (*str != '\0')
	{
		if (*str >= 'A' && *str <= 'Z')
			*str = (*str - 'A' + rot_value) % 26 + 'A';
		else if (*str >= 'a' && *str <= 'z')
			*str = (*str - 'a' + rot_value) % 26 + 'a';
		else if (*str >= '0' && *str <= '9')
			*str = (*str - '0' + rot_value) % 10 + '0';
		str++;
	}
	return (start);
}
