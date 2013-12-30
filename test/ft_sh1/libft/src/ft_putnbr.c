/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 16:57:30 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 22:30:12 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	ft_putnbr(long n)
{
	char	*number;

	number = ft_itoa_base(n, 10, "0123456789");
	ft_putstr(number);
	free(number);
}

