/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 18:08:11 by ksever            #+#    #+#             */
/*   Updated: 2013/12/21 21:37:50 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	ft_putnbr_fd(long n, int fd)
{
	char	*number;

	number = ft_itoa_base(n, 10, "0123456789");
	ft_putstr_fd(number, fd);
	free(number);
}

