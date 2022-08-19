import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **key):
    balls = key 
    self.contents = [] 

    for ball, n in balls.items(): 
      for index in range(n):
        self.contents.append(ball)     

  def draw(self, draws):
    n = 0
    draws_list = [] 

    if draws > len(self.contents): 
      limit = len(self.contents) 
      
    else: 
      limit = draws 
    
    while n < limit: 
      draws_list.append(self.contents.pop(random.randrange(0, len(self.contents))))
      n += 1
    
    return draws_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  exp = num_experiments

  i = 0
  M = 0 

  while i < exp:
    balls_list = hat.contents.copy()
    results_list = []
    results_count = {}
   
    if num_balls_drawn > len(balls_list): 
      limit = len(balls_list)
      
    else: 
      limit = num_balls_drawn
      
    n = 0
    while n < limit: 
      results_list.append(balls_list.pop(random.randrange(0, len(balls_list))))
      n += 1 
    
    for ball in results_list:
      results_count[ball] = results_list.count(ball)
    
    expected_counter = 0
    for ball in expected_balls.keys(): 

      try:
        if results_count[ball] >= expected_balls[ball]: 
          expected_counter += 1 
      except: 
        pass 

    if expected_counter == len(expected_balls):
      M += 1   

    i += 1


  return M / exp
  