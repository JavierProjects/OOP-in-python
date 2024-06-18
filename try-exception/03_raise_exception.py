def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    # Alternatives: raise TypeError() or TypeError('Message')
    raise TypeError('Employee does not have access!')

open_register('Authorized')
open_register('Not Authorized')