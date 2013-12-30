/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putaddress.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 16:57:30 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:37:14 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void		ft_putaddress(void *ptr)
{
	unsigned long		nbr;
	char				*address;

	nbr = (unsigned long)ptr;
	address = ft_itoa_base_unsigned(nbr, 16, "0123456789abcdef");
	ft_putstr("0x");
	ft_putstr(address);
	free(address);
}

