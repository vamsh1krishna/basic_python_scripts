
def arithmetic_arranger(problems):


    if len(problems) > 4 :
        return "Error: Too many problems."

    new_problems = []


    line1 = []
    line2 = []
    line3 = []
    answers = []


    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}


    for query in problems:
        parts = query.split()
        new_problems.append(parts)



    for single_prob in new_problems:


        if single_prob[1] not in ops.keys():
            return "Error: Operator must be '+' or '-'."


        if not str(single_prob[0]).isnumeric() or not str(single_prob[2]).isnumeric():
            return "Error: Numbers must only contain digits."


        if len(single_prob[0]) > 4 or len(single_prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."




        char_limit = int(len(single_prob[0]))
        if len(single_prob[0]) <= len(single_prob[2]):
            char_limit = int(len(single_prob[2]))


        pretty_num1 = str(single_prob[0]).rjust(char_limit+2)
        line1.append(pretty_num1)


        pretty_sec_elemem = (str(single_prob[1])+' '+str(single_prob[2])).rjust(char_limit+2)
        line2.append(pretty_sec_elemem)



        if single_prob[1] in ops.keys():
            single_ans = ops[single_prob[1]](int(single_prob[0]),int(single_prob[2]))
        else:
            pass


        pretty_ans = str(single_ans).rjust(char_limit+2)
        answers.append(pretty_ans)


        line3.append('-'*(char_limit+2))






    line1string = '    '.join(line1)
    line2string = '    '.join(line2)
    line3string = '    '.join(line3)
    answersstring = '    '.join(answers)





    finallist = [line1string, line2string, line3string, answersstring]






    outputanswer = "\n".join(finallist)

    return outputanswer


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
