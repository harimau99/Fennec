/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cos.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/18 16:35:25 by ksever            #+#    #+#             */
/*   Updated: 2013/12/18 17:32:56 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

double	ft_cos(double ang)
{
	double		cosinus;

	ang += 1.57079632;
	if (ang > 3.14159265)
		ang -= 6.28318531;
	if (ang < 0)
	{
		cosinus = 1.27323954 * ang + 0.405284735 * ang * ang;
		if (cosinus < 0)
			cosinus = 0.225 * (cosinus * (-cosinus) - cosinus) + cosinus;
		else
			cosinus = 0.225 * (cosinus * cosinus - cosinus) + cosinus;
	}
	else
	{
		cosinus = 1.27323954 * ang - 0.405284735 * ang * ang;
		if (cosinus < 0)
			cosinus = 0.225 * (cosinus * (-cosinus) - cosinus) + cosinus;
		else
			cosinus = 0.225 * (cosinus * cosinus - cosinus) + cosinus;
	}
	return (cosinus);
}
