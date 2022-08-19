def arithmetic_arranger(problems,result=False):
  if len(problems) > 5: 
    return 'Error: Too many problems.'

  first_list = []
  second_list = [] 
  div_list =[]
  ans_list = [] 
  
  for problem in problems: 
    eq_list = problem.strip().split(' ')

    if len(eq_list[0]) > 4 or len(eq_list[2]) > 4: 
      return 'Error: Numbers cannot be more than four digits.'
      
    if eq_list[1] != '+' and eq_list[1] != '-':
      return "Error: Operator must be '+' or '-'."
    
    try: 
      operand_one = int(eq_list[0])
    except: 
      return 'Error: Numbers must only contain digits.'

    try: 
      operand_two = int(eq_list[2])
    except: 
      return 'Error: Numbers must only contain digits.'

    if eq_list[1] == '+':
      ans = operand_one + operand_two

    if eq_list[1] == '-':
      ans = operand_one - operand_two

    if len(eq_list[0]) > len(eq_list[2]):
      eq_len = len(eq_list[0]) + 2
      eq_list[0] = eq_list[0].rjust(eq_len)
      eq_list[2] = eq_list[1] + eq_list[2].rjust(eq_len - 1)

      div_len = eq_len * '-'

      ans = f'{ans}'.rjust(eq_len)
      
    else: 
      eq_len = len(eq_list[2]) + 2
      eq_list[0] = eq_list[0].rjust(eq_len)
      eq_list[2] = eq_list[1] + ' ' + eq_list[2]

      div_len = eq_len * '-'

      ans = f'{ans}'.rjust(eq_len)
    
    first_list.append(eq_list[0])      
    second_list.append(eq_list[2])
    div_list.append(div_len)
    ans_list.append(ans)

  first_string = '    '.join(first_list)
  second_string = '    '.join(second_list)
  div_string = '    '.join(div_list)
  ans_string = '    '.join(ans_list)

  if result == True:
    arranged_problems = first_string + '\n' + second_string + '\n' + div_string + '\n' + ans_string
  
  else: 
    arranged_problems = first_string + '\n' + second_string + '\n' + div_string
  
  return arranged_problems


"""
1. Check length of problems input to determine if it is greater than 5 
  a) If yes, return Error
NOTE: Create a For Loop to iterate through each Element & .strip() them 
2. problems.split(' ') to separate string into 1st operand, operator, and 2nd operand string list 
3. Check if operator is + or -
  a) If no, return Error 
4. Check is operands are integers
  a) If no, return Error 
5. Check length of operand to determine if it is greater than 4 
  a) If yes, return Error 
6. Determine the total length of the arithmetic problem 
  a) lenth of longest operand + 2 (For Operator & Space)
7. Add leading spaces using rjust() to get strings eqaul to total length 
8. Create a string of underscores (_) equal to total length 
9. Join each arithmetic problems together using 4 spaces (    ) 
10. Convert operands to integers to perform calculations 
11. Determine arithmetic problems using operator 
12. Create a string to result of arithmetic
13. Include in final string if ans=True
"""