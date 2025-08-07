import time
import locale
import sys

name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s!' % name)

try:
    if sys.platform.startswith('win'):
        locale.setlocale(locale.LC_TIME, 'german')
    else:
        locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
except locale.Error:
    print("Warnung: Deutsche Lokalisierung konnte nicht gesetzt werden.")

heutiges_datum = time.strftime('Heute ist %A, der %d. %B.')
print(heutiges_datum)
