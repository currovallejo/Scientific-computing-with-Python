import re

def arithmetic_arranger(problems, results=False):

  # check there are not more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # check operators
  n_addition = 0
  n_substraction = 0
  for problem in problems:
    if re.search('\+', problem):
      n_addition += 1
    elif re.search('-', problem): 
      n_substraction += 1

  if n_addition + n_substraction != len(problems):
    return "Error: Operator must be '+' or '-'."

  # check digits
  for problem in problems:
    b = re.findall('[0-9]+', problem)
    n_digits = 0
    for i in b:
      n_digits += len(i)
    if n_digits != len(problem) - 3:
      return "Error: Numbers must only contain digits."

  # check max 4 digits
    for problem in problems:
      b = re.findall('[0-9]+', problem)
      n_digits = 0
      for i in b:
        if len(i) > 4:
          return "Error: Numbers cannot be more than four digits."

  # variables definition
  upper_string = ''
  lower_string = ''
  line_string = ''
  results_string = ''
  numbers = []

  # string building
  for i, problem in enumerate(problems):
    numbers.append(re.findall('[0-9]+', problem))
    operator = re.findall('[+-]', problem)
    operator = operator[0]
    for pair in numbers:
      upper_number = pair[0]
      lower_number = pair[1]
      max_len = (max(len(number) for number in pair))

    if i != 0:
      upper_string += ' ' * 4
      lower_string += ' ' * 4
      line_string += ' ' * 4
      results_string += ' ' * 4

    upper_string += ' ' * 2 + ' ' * (max_len - len(upper_number)) + upper_number
    lower_string += operator + ' ' + ' ' * (max_len - len(lower_number)) + lower_number
    line_string += '--' + '-' * max_len
    if operator == '+':
      results_string += ' ' + ' '*(1+max_len-len(str(int(upper_number) + int(lower_number)))) + str(int(upper_number) + int(lower_number))
    else:
      if int(upper_number) - int(lower_number)<0:
        results_string += ' ' + ' '*(max_len-len(str(int(upper_number) - int(lower_number)))) + str(int(upper_number) - int(lower_number))
      else:
        results_string += ' ' + ' '*(1+max_len-len(str(int(upper_number) - int(lower_number)))) + str(int(upper_number) - int(lower_number))

  if results == True:
    arranged_problems = upper_string + '\n' + lower_string + '\n' + line_string + '\n' + results_string
  else:
    arranged_problems = upper_string + '\n' + lower_string + '\n' + line_string

  return arranged_problems
