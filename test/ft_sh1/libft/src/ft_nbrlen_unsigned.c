/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_nbrlen_unsigned.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/07 17:17:12 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 21:31:09 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

size_t		ft_nbrlen_unsigned(unsigned long nbr, unsigned long base)
{
	size_t		len;

	len = 1;
	while ((nbr / base) != 0)
	{
		nbr = nbr / base;
		len++;
	}
	return (len);
}
