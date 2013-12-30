/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdel.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/26 16:18:50 by ksever            #+#    #+#             */
/*   Updated: 2013/12/06 15:51:49 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	ft_lstdel(t_list **alst, void (*del)(void *, size_t))
{
	t_list	*list;
	t_list	*to_del;

	if (alst && *alst)
	{
		list = *alst;
		while (list)
		{
			to_del = list;
			list = list->next;
			del(to_del->content, to_del->content_size);
			free(to_del);
			to_del = NULL;
		}
	}
	*alst = NULL;
}

