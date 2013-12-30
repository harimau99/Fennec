/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_nbrmag_unsigned.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/21 20:22:57 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:42:00 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned long	ft_nbrmag_unsigned(unsigned long nbr, unsigned long base)
{
	long		mag;

	mag = 1;
	while (nbr / base != 0)
	{
		mag = mag * base;
		nbr = nbr / base;
	}
	return (mag);
}
