/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstswap.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/13 17:49:24 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 18:11:10 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_bool	ft_lstswap(t_list **head, t_list **node1, t_list **node2)
{
	t_list		*tmp;
	t_list		*prev1;
	t_list		*prev2;

	if (!(*head) || !(*node1) || !(*node2))
		return (false);
	prev1 = ft_lstprevious(*head, *node1);
	prev2 = ft_lstprevious(*head, *node2);
	if (prev1)
		prev1->next = *node2;
	if (prev2)
		prev2->next = *node1;
	tmp = (*node1)->next;
	(*node1)->next = (*node2)->next;
	(*node2)->next = tmp;
	if ((*head) == (*node1))
		*head = *node2;
	else if ((*head) == (*node2))
		*head = *node1;
	return (true);
}
