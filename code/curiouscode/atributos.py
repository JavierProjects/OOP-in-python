# Atributos
# Los atributos de clase son variables que se definen fuera de todos los métodos y tienen el mismo valor para cada instancia de la clase. 

# También se puede acceder a ellos a través del nombre de la clase en lugar del nombre de la instancia. 

# Ajustar un atributo (variable) a través del nombre de la clase lo cambiará para todas las instancias.

# Nota: Ajustar el atributo mediante un nombre de instancia interrumpirá la conexión para esa instancia; es decir, aunque posteriormente el atributo se modifique via la clase el atributo de la instancia modificada anteriormente no sufrira cambio (actualizacion).

class Bird:
  # Class attribute
  hungry_level = 3

# Accesar el atributo via la instancia
parakeet = Bird() # Perico
parrot = Bird() # Loro

print(parakeet.hungry_level) # 3
print(parrot.hungry_level) # 3

# Accesar el atributo via la clase
print(Bird.hungry_level) # 3

# Ajustar el atributo via la clase 
# alterara todas las instancias
print("Se cambio el atributo 'hungry_level' de las clase 'Bird'")
Bird.hungry_level = 4

print(parakeet.hungry_level) # 4
print(parrot.hungry_level) # 4

# Accesar el atributo via la clase
print(Bird.hungry_level) # 4

# Se ajusto una instancia
print("Se ajusto una instancia")
parakeet.hungry_level = 5

print(parakeet.hungry_level) # 5
print(parrot.hungry_level) # 4

# Accesar el atributo via la clase
print(Bird.hungry_level) # 4

# Ajustar el atributo via la clase 
# alterara todas las instancias
print("Se cambio el atributo 'hungry_level' de las clase 'Bird'")
Bird.hungry_level = 1

print(parakeet.hungry_level) # 5
print(parrot.hungry_level) # 1

# Accesar el atributo via la clase
print(Bird.hungry_level) # 1