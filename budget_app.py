class Category:

  def __init__(self, category):
    self.category = category 
    self.ledger = []

  def __str__(self): 
    title = self.category.center(30, '*')

    item_list = []

    for line in self.ledger: 
      item_desc = line['description'][0:23].ljust(23)
      
      item_amount_str = f"{line['amount']:.3f}"
      item_amount = item_amount_str[-8:-1].rjust(7)

      item = f'{item_desc}{item_amount}'

      item_list.append(item)

    item_str = '\n'.join(item_list) 

    total_str = f'Total: {self.get_balance()}'

    final_str = title + '\n' + item_str + '\n' + total_str

    return final_str

  def deposit(self, amount, desc=''): 
    self.ledger.append({'amount': amount, 'description': desc})

  def withdraw(self, amount, desc=''):

    balance = self.get_balance()

    if balance - amount >= 0: 
      neg_amount = amount * -1
      self.ledger.append({'amount': neg_amount, 'description': desc})
      return True

    else: 
      return False 

  def get_balance(self): 
    balance = 0
    
    for line in self.ledger: 
      balance += line['amount']

    return balance 

  def transfer(self, amount, other):

    if self.get_balance() - amount >= 0: 
      other.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
      
      neg_amount = amount * -1
      self.ledger.append({'amount': neg_amount, 'description': f'Transfer to {other.category}'})

      return True 
    
    else:

      return False

  def check_funds(self, amount): 
    
    if self.get_balance() - amount >= 0: 
      return True

    else: 
      return False


def create_spend_chart(categories):  
  import math 

  ### Title 
  title = 'Percentage spent by category'

  # Side Legend List
  leg_list = []
  leg_start = 100 
  while leg_start >= 0: 
    leg_list.append(f'{leg_start}|'.rjust(4))
    leg_start -= 10

  # Money Spent by Categories 
  spent_list = []
  for category in categories: 
    cat_spent = 0
    for item in category.ledger:
      if item['amount'] < 0:         
        cat_spent += item['amount']
        
    spent_list.append(cat_spent)

  # Total Money Spent 
  total_spent = sum(spent_list)

  # Convert Money Spent to Percentage Spent by Categories 
  percent_list = [] 
  for spent in spent_list: 
    percent_list.append(math.ceil((spent/total_spent) * 10))

  ### Create Legends + o Rows of Percentages for Graph 
  cat_col_list = []
  for percent in percent_list: 
    index = 0 
    index_list = [] 
    while index < 11: 
      index_list.append(" ")
      index += 1
    
    o_index = -1
    while o_index >= (-1 * percent): 
      index_list[o_index] = 'o'
      o_index -= 1

    cat_col_list.append(index_list)

  o_row_list = [] 
  for i in range(11): 
    row = " "
    for col in cat_col_list: 
      row += col[i] + '  '

    o_row_list.append(row) 

  new_row_list = []
  for i in range(11): 
    new_row = leg_list[i] + o_row_list[i]
    new_row_list.append(new_row)

  ### Bottom Divider 
  div_len = len(o_row_list[0])
  div = '\n' + '    ' + ('-' * div_len)

  ### Vertical Category Name
  cat_len_list = []
  for cat in categories:
    cat_name_len = len(cat.category)
    cat_len_list.append(cat_name_len)

  max_cat_len = max(cat_len_list)

  new_cat_list = [] 
  for cat in categories:
    new_cat_name = cat.category.ljust(max_cat_len)
    new_cat_list.append(new_cat_name)

  cat_row_list = [] 
  for i in range(max_cat_len): 
    cat_row = ''
    for col in new_cat_list: 
      cat_row += col[i] + '  '
    
    cat_row_list.append('     ' + cat_row) 


  
  """
NOTE: Vertical Category Names 
  1. create list of the length of each category 
  2. find greatest length 
  3. create another list of each category, but apply ljust(greatest length) to all 
  4. Create a list of rows of category names written vertically 

NOTE: Bottom Divider 
  1. Create a string of 4 spaces '    '
  2. Create a divider of '-' as long as the length of columns 
    a) '-' * len(col) 
  3. Add to percentage table 
  
  """
  graph_str = '' 
  for row in new_row_list: 
    graph_str += '\n' + row

  cat_name_str = ''
  for row in cat_row_list: 
    cat_name_str += '\n' + row

  chart_str = title + graph_str + div + cat_name_str
  
  return chart_str
  

  
  
  #create each legend value by making a for loop to iterate through each and make the appropriate size. 

  #legend can be iterated using a variable += and converting to string 
