/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstcount.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/13 17:27:50 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 17:39:30 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h"

size_t		ft_lstcount(t_list *node)
{
	size_t	count;

	count = 0;
	while (node)
	{
		count++;
		node = node->next;
	}
	return (count);
}
