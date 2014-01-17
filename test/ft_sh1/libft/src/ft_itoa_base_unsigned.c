/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base_unsigned.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/24 19:00:16 by ksever            #+#    #+#             */
/*   Updated: 2014/01/17 21:07:51 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char		*ft_itoa_base_unsigned(unsigned long n,
									unsigned long base, char *digits)
{
	char			*res;
	char			*save;
	unsigned long	mag;

	if (!(res = (char *)malloc(sizeof(char)
								* (ft_nbrlen_unsigned(n, base) + 1))))
		return (NULL);
	save = res;
	mag = ft_nbrmag_unsigned(n, base);
	while (mag > 0)
	{
		*res++ = digits[n / mag];
		n = n % mag;
		mag = mag / base;
	}
	*res = '\0';
	return (save);
}

