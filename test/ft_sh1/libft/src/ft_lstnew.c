/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/24 22:01:08 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 17:04:49 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

t_list		*ft_lstnew(const void *content, size_t content_size)
{
	t_list		*newnode;

	newnode = (t_list *)malloc(sizeof(t_list));
	if (!newnode)
		return (NULL);
	newnode->next = NULL;
	newnode->content_size = (!content ? 0 : content_size);
	if (!content || content_size == 0)
	{
		newnode->content = NULL;
		return (newnode);
	}
	newnode->content = ft_memalloc(content_size);
	if (newnode->content == NULL)
	{
		free(newnode);
		return (NULL);
	}
	ft_memcpy(newnode->content, content, content_size);
	return (newnode);
}

