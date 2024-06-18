instrument_familes = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

def print_instrument_families():
  for family in ['Strings', 'Percussion', 'woodwinds']:
    print('Some instruments in the ' + family + 'family are: ' + instrument_familes[family])

try:
  print_instrument_families()
except TypeError:
  print('La funcion print no acepta listas')  
