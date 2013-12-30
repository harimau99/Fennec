/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstappend.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/13 17:07:37 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 17:19:28 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void		ft_lstappend(t_list **alst, t_list *newnode)
{
	t_list		*current;

	if ((*alst) == NULL)
	{
		*alst = newnode;
		return ;
	}
	current = *alst;
	while (current->next)
		current = current->next;
	current->next = newnode;
}
