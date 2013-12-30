/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstprepend.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/26 18:09:06 by ksever            #+#    #+#             */
/*   Updated: 2013/12/13 17:08:52 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstprepend(t_list **alst, t_list *newnode)
{
	if (alst && *alst)
	{
		newnode->next = *alst;
		*alst = newnode;
	}
	if (alst && !(*alst))
	{
		*alst = newnode;
	}
}

