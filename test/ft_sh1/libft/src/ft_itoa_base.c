/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/24 19:00:16 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:40:05 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char		*ft_itoa_base(long n, long base, char *digits)
{
	char		*res;
	char		*save;
	long		mag;
	long		is_neg;
	long		digidx;

	if (!(res = (char *)malloc(sizeof(char) * (ft_nbrlen(n, base) + 1))))
		return (NULL);
	save = res;
	is_neg = (n < 0 ? -1 : 1);
	if (n < 0)
		*res++ = '-';
	mag = ft_nbrmag(n, base);
	while (mag > 0)
	{
		digidx = n / (mag * is_neg);
		*res++ = digits[digidx];
		n = n % mag;
		mag = mag / base;
	}
	*res = '\0';
	return (save);
}

