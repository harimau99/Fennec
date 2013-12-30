/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ksever <ksever@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2013/11/19 14:05:12 by ksever            #+#    #+#             */
/*   Updated: 2013/12/27 00:07:34 by ksever           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>

# define PI 3.14159265358979323846
# define GNL_BUFF_SIZE 4096

# ifndef FT_T_BOOL
#  define FT_T_BOOL

typedef enum		e_bool
{
	false,
	true
}					t_bool;

# endif /* !FT_T_BOOL */

typedef struct		s_list
{
	void			*content;
	size_t			content_size;
	struct s_list	*next;
}					t_list;

void			ft_bzero(void *s, size_t n);
void			*ft_memset(void *b, int c, size_t len);
void			*ft_memcpy(void *s1, const void *s2, size_t n);
void			*ft_memccpy(void *s1, const void *s2, int c, size_t n);
void			*ft_memmove(void *s1, const void *s2, size_t n);
void			*ft_memchr(const void *s, int c, size_t n);
int				ft_memcmp(const void *s1, const void *s2, size_t n);
void			*ft_memalloc(size_t size);
void			ft_memdel(void **ap);
t_bool			ft_isalpha(int c);
t_bool			ft_isdigit(int c);
t_bool			ft_isalnum(int c);
t_bool			ft_isascii(int c);
t_bool			ft_isprint(int c);
t_bool			ft_isspace(int c);
int				ft_toupper(int c);
int				ft_tolower(int c);
size_t			ft_strlen(const char *s);
size_t			ft_strclen(const char *s, char srch);
char			*ft_strdup(const char *s1);
char			*ft_strcpy(char *s1, const char *s2);
char			*ft_strncpy(char *s1, const char *s2, size_t n);
char			*ft_strcat(char *s1, const char *s2);
char			*ft_strncat(char *s1, const char *s2, size_t n);
size_t			ft_strlcat(char *dst, const char *src, size_t size);
char			*ft_strchr(const char *s, int c);
char			*ft_strrchr(const char *s, int c);
char			*ft_strstr(const char *s1, const char *s2);
char			*ft_strnstr(const char *s1, const char *s2, size_t n);
int				ft_strcmp(const char *s1, const char *s2);
int				ft_strncmp(const char *s1, const char *s2, size_t n);
char			*ft_strnew(size_t size);
void			ft_strdel(char **as);
void			ft_strclr(char *s);
void			ft_striter(char *s, void (*f)(char *));
void			ft_striteri(char *s, void (*f)(unsigned int, char *));
char			*ft_strmap(const char *s, char (*f)(char));
char			*ft_strmapi(const char *s, char (*f)(unsigned int, char));
t_bool			ft_strequ(const char *s1, const char *s2);
t_bool			ft_strnequ(const char *s1, const char *s2, size_t n);
char			*ft_strsub(const char *s, unsigned int start, size_t n);
char			*ft_strjoin(const char *s1, const char *s2);
char			*ft_strjoinwithglue(const char *s1, const char *s2, char glue);
char			*ft_strtrim(const char *s);
char			**ft_strsplit(const char *s, char c);
char			*ft_strrev(char *s);
char			*ft_rotalnum(char *str, int rot_value);
int				ft_atoi(const char *str);
char			*ft_itoa(long n);
char			*ft_itoa_base(long n, long base, char *digits);
char			*ft_itoa_base_unsigned(unsigned long n,
										unsigned long base, char *digits);
size_t			ft_nbrlen(long nbr, long base);
size_t			ft_nbrlen_unsigned(unsigned long nbr, unsigned long base);
long			ft_nbrmag(long n, long base);
unsigned long	ft_nbrmag_unsigned(unsigned long  n, unsigned long base);
void			ft_putchar(char c);
void			ft_putchar_fd(char c, int fd);
void			ft_putstr(const char *s);
void			ft_putstr_fd(const char *s, int fd);
void			ft_putnstr(char const *s, size_t limit);
void			ft_putendl(const char *s);
void			ft_putendl_fd(const char *s, int fd);
void			ft_putnbr(long nbr);
void			ft_putnbr_fd(long nbr, int fd);
void			ft_putnbr_base(long nbr, long base, char *digits);
void			ft_putnbr_base_unsigned(unsigned long nbr,
										unsigned long base, char *digits);
void			ft_putaddress(void *ptr);
void			ft_putaddress_fd(void *ptr, int fd);
int				ft_get_next_line(const int fd, char **line);
t_list			*ft_lstnew(const void *content, size_t content_size);
void			ft_lstdelone(t_list **alst, void (*del)(void *, size_t));
void			ft_lstdel(t_list **alst, void (*del)(void *, size_t));
void			ft_lstprepend(t_list **alst, t_list *newnode);
void			ft_lstappend(t_list **alst, t_list *newnode);
size_t			ft_lstcount(t_list *node);
t_list			*ft_lstprevious(t_list *head, t_list *srch);
t_bool			ft_lstswap(t_list **head, t_list **node1, t_list **node2);
void			ft_lstiter(t_list *lst, void (*f)(t_list *elem));
t_list			*ft_lstmap(t_list *lst, t_list *(*f)(t_list *elem));
t_bool			ft_fs_isdotordotdot(const char *str);
t_bool			ft_fs_path_isvalid(const char *str);
char			*ft_fs_path_join(const char *prefix, const char *path);
char			*ft_fs_path_dirname(const char *path);
double			ft_degtorad(double deg);
double			ft_sin(double ang);
double			ft_cos(double ang);
long			ft_abs(long nbr);

#endif /* !LIBFT_H */

