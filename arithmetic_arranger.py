def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for index, value in enumerate(problems):
        operation = value.split(" ")

        if operation[1] not in "-+":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        try:
            value_1 = int(operation[0])
            value_2 = int(operation[2])
        except ValueError:
            return "Error: Numbers must only contain digits."


        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2

      

        Line_1 = f"{operation[0]:>{width}}"
        Line_2 = operation[1] + f"{operation[2]:>{width-1}}"
        Dashes = '-' * width
        

        try:
          arranged_problems[0] += (' ' * 4) + Line_1
        except IndexError:
          arranged_problems.append(Line_1)

        try:
          arranged_problems[1] += (' ' * 4) + Line_2
        except IndexError:
          arranged_problems.append(Line_2)

        try:
          arranged_problems[2] += (' ' * 4) + Dashes
        except IndexError:
          arranged_problems.append(Dashes)


        if args:
          
          answer = int(operation[0]) + int(operation[2]) if operation[1] == '+' else int(operation[0]) - int(operation[2])
          ans = f"{str(answer):>{width}}"

          try:
            arranged_problems[3] += (' ' * 4) + ans
          except IndexError:
            arranged_problems.append(ans)


    result = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    result = result + f"\n{arranged_problems[3]}" if args else result

    return result
