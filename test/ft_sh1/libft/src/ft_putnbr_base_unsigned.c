/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base_unsigned.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 16:57:30 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:36:12 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	ft_putnbr_base_unsigned(unsigned long nbr,
								unsigned long base, char *digits)
{
	char	*number;

	number = ft_itoa_base_unsigned(nbr, base, digits);
	ft_putstr(number);
	free(number);
}
