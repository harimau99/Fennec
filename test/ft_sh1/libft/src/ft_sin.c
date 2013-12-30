/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sin.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/18 16:35:25 by ksever            #+#    #+#             */
/*   Updated: 2013/12/18 17:16:03 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

double	ft_sin(double ang)
{
	double		sinus;

	if (ang < -3.14159265)
		ang += 6.28318531;
	else if (ang > 3.14159265)
		ang -= 6.28318531;
	if (ang < 0)
	{
		sinus = 1.27323954 * ang + 0.405284735 * ang * ang;
		if (sinus < 0)
			sinus = 0.225 * (sinus * (-sinus) - sinus) + sinus;
		else
			sinus = 0.225 * (sinus * sinus - sinus) + sinus;
	}
	else
	{
		sinus = 1.27323954 * ang - 0.405284735 * ang * ang;
		if (sinus < 0)
			sinus = 0.225 * (sinus * (-sinus) - sinus) + sinus;
		else
			sinus = 0.225 * (sinus * sinus - sinus) + sinus;
	}
	return (sinus);
}
