/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sh_tablen.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/27 15:38:43 by ksever            #+#    #+#             */
/*   Updated: 2013/12/27 15:41:36 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

size_t		ft_sh_tablen(char **tab)
{
	size_t		length;

	length = 0;
	while (tab[length])
		length++;
	return (length);
}
