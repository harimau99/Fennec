/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstprevious.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/13 17:40:57 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 17:47:18 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list		*ft_lstprevious(t_list *head, t_list *srch)
{
	t_list		*current;

	if (!head || !srch)
		return (NULL);
	if (head == srch)
		return (NULL);
	current = head;
	while (current->next)
	{
		if (current->next == srch)
			return (current);
		current = current->next;
	}
	return (NULL);
}
