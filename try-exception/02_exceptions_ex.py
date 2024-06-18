# Este codigo lanza 2 exceptions

# Traceback (most recent call last):
#   File "/Users/javierromero/repos/OOP/testing/02_exceptions_ex.py", line 5, in <module>
#     print('The following ' + len(sale_instruments) + ' instruments are on sale:')
# TypeError: must be str, not int

# Traceback (most recent call last):
#   File "/Users/javierromero/repos/OOP/testing/02_exceptions_ex.py", line 15, in <module>
#     print(sale_instruments[3])
# IndexError: list index out of range

sale_instruments = ['Violin', 'Conga', 'Clavinet']

print('The following ' + len(sale_instruments) + ' instruments are on sale:')
print(sale_instruments[0])
print(sale_instruments[1])
print(sale_instruments[3])
