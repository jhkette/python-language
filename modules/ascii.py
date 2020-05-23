
from termcolor import colored
# importing colored from termcolor

from pyfiglet import Figlet
# import figlet from pyfiglet

x = input('input your cool text here: ')
f = Figlet(font='slant')
print(colored(f.renderText(x), color="magenta"))

