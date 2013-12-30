/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_shell.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/12/23 19:17:32 by ksever            #+#    #+#             */
/*   Updated: 2013/12/29 01:06:48 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_SHELL_H
# define FT_SHELL_H

# include <unistd.h>

size_t		ft_sh_tablen(char **tab);
int			ft_sh_error(char *error);
int			ft_sh_perror(char *error);
int			ft_sh_init(void);
char		*ft_sh_prompt(void);
int			ft_sh_dispatch(char *cmd);
void		ft_sh_signal_handler(int sigid);
int			ft_cmd_exit(char **args);
int			ft_cmd_env(char **argv);
int			ft_cmd_env_show(void);
int			ft_cmd_env_srch(char *key);
int			ft_cmd_env_set(char *key, char *value);
char		*ft_cmd_env_get(char *key);
int			ft_cmd_env_append(char *key, char *value);
int			ft_cmd_setenv(char **argv);
int			ft_cmd_unsetenv(char **argv);
int			ft_cmd_cd(char **argv);
int			ft_cmd_cd_home(void);
int			ft_cmd_cd_oldpwd(void);
int			ft_cmd_cd_goto(char *path);
int			ft_cmd_spawn(char **argv, char *path);

extern char			**environ;
extern char			**g_shenv;
extern pid_t		g_currproc;

typedef struct		s_fptr
{
	char		*cmd;
	int			(*fct)(char **argv);
}					t_fptr;

#endif /* !FT_SHELL_H */
