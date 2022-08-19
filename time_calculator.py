def add_time(start, duration, dow=None):
  time_list = start.split(' ')
  time_list[0] = time_list[0].split(':')

  if time_list[1] == 'PM' and time_list[0][0] == '12':
    time_list[0][0] == '00'
    
  if time_list[1] == 'AM' and time_list[0][0] == '12':
    time_list[0][0] == '00'
  
  if time_list[1] == 'PM':
    current_hr = int(time_list[0][0]) + 12
    current_min = int(time_list[0][1])
    
  else:
    current_hr = int(time_list[0][0])
    current_min = int(time_list[0][1])

  dura_list = duration.split(':') 

  dura_hr = int(dura_list[0])
  dura_min = int(dura_list[1])

  total_hr = current_hr + dura_hr
  total_min = current_min + dura_min 

  if total_min/60 >= 1:
    total_hr += 1 
    total_min -= 60

  n_counter = 0 
  while total_hr/24 >= 1: 
    total_hr -= 24 
    n_counter += 1 

  if total_hr == 12:
    new_time = f'{total_hr}:{total_min:02d} PM'
    
  elif total_hr > 12: 
    total_hr -= 12
    new_time = f'{total_hr}:{total_min:02d} PM'
    
  elif total_hr == 0:
    new_time = f'12:{total_min:02d} AM'

  else: 
    new_time = f'{total_hr}:{total_min:02d} AM'

  dow_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
  
  if dow != None: 
    dow = dow.lower()
    current_index = dow_list.index(dow) 
    index_counter = current_index + n_counter
    
    while index_counter >= 7:
      index_counter -= 7 

    new_dow = dow_list[index_counter].capitalize()

    new_time = f'{new_time}, {new_dow}'
    

  if n_counter == 1: 
    new_time = f'{new_time} (next day)'

  elif n_counter >= 2: 
    new_time = f'{new_time} ({n_counter} days later)'

  

  
  return new_time

"""
NOTE: Break code into 3 separate parts 
NOTE 2: Hours will be on a 24 base & minutes will be on a 60 base

  1. Scenario where time add is within day
  2. Scenario where time add results in another day 
  3. Scenario where time & day of week is inputted 

1. start.split(' ') to separate time and AM/PM 
2. time.split(':') to separate hour and minute
3. convert hour to its equivalent 24-hour value & set to variable
  a) PM will add 12 to hours 
4. set minute to a varialble
5. duration.split(':') to separate hour and minutes 
6. add duration.hour to time.hour 
7. add duration.minute to time.minute
8. Determine if addition is over the base limits of hour and minute 
  a) if yes, add necessary conversion and indicators 
9. Day of Week will be put into a list
10. index of day list will determine location of the day 
11. If index value change, day of week will follow suit 
"""