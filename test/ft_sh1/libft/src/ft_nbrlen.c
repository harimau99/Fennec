/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_nbrlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/07 17:17:12 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 21:30:50 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

size_t		ft_nbrlen(long nbr, long base)
{
	size_t		len;

	len = 1;
	if (nbr < 0)
		len++;
	while ((nbr / base) != 0)
	{
		nbr = nbr / base;
		len++;
	}
	return (len);
}
