import re # regular expression

def arithmetic_arranger(problems,solve=False):
  if len(problems)>5:
    return "Error: Too many problems."
  
  num1=""
  num2=""
  lines=""
  sums=""
  # the final report
  for problem in problems:
    temp_list=problem.split()
    num=temp_list[0]
    oper=temp_list[1]
    deno=temp_list[2]

    #errors detector
    if oper == "*" or oper == "/":
      return "Error: Operator must be '+' or '-'."
      
    if re.search("[^\d]",num) or re.search("[^\d\+\-]",deno):
      return "Error: Numbers must only contain digits."

    if len(num)>4 or len(deno)>4 :
      return "Error: Numbers cannot be more than four digits."

    #answer format
    res=""
    if oper=="+":
      res = str(int(num)+int(deno))
    elif oper == "-":
      res = str(int(num)-int(deno))

    size = max(len(num),len(deno))+2

    num_line = ""
    num_line = str(num.rjust(size))
    deno_line = ""
    deno_line = str(oper) + str(deno.rjust(size - 1))

    #dash line creation
    dash_lines = ""
    for p in range(size):
      dash_lines += "-"
      
    #results lines
    res_line = ""
    res_line += res.rjust(size)

    #format structuring
    if problem != problems[-1]:
      num1 += num_line + "    "
      num2 += deno_line + "    "
      lines += dash_lines + "    "
      sums += res_line + "    "
    else:
      num1 += num_line
      num2 += deno_line
      lines += dash_lines
      sums += res_line 


  if solve == True:
    arranged_line = num1 + "\n" + num2 + "\n" + lines + "\n" + sums
  else:
    arranged_line = num1 + "\n" + num2 + "\n" + lines 
    
  return arranged_line
