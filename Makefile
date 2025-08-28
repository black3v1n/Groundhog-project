##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## makefile
##

SRC	=	$(shell find ./src -name '*py')

MAIN = 	$(shell find -name 'main.py')

NAME	=	groundhog

all:
	touch $(NAME)
	cp $(MAIN) $(NAME)
	chmod +x $(NAME)

clean:
	$(RM) $(NAME)
	$(RM) -r src/__pycache__

fclean: clean

re: fclean all
