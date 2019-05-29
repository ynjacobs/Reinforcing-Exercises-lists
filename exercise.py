ints = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def print_empty_seats(row, number):
  counter = 1
  for seat in row:
    if not seat:
      print('Row {} seat {} is free. Do you want to sit there? (y/n) '.format(number, counter))
      if is_yes(input()):
       row[counter -1] = input('What is your name?')
    counter += 1

def is_yes(answer):  
  if answer[0].lower() == 'y':
    return True
  else:
    return False

# MAIN 



counter = 1
for row in ints:
  print_empty_seats(row, counter)
  counter += 1
print(ints)
   



  