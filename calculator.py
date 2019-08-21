#  -3*(4+5*6)/17     ->-6

class Calculator:
    @staticmethod
    def calc(expression):
        def calc_sub(sub_expression):
            #计算"源表达式" ,两个操作数 一个操作符
            def get_ans(num_left,num_right,op):
                if(op=="+"):
                    return num_left+num_right
                elif(op=="-"):
                    return num_left-num_right
                elif(op=="*"):
                    return num_left*num_right
                elif(op=="/"):
                    return num_left/num_right
            # (-4*52+3)
            op_map={"*":4,"/":4,"+":2,"-":2,"(":0}
            op_stack=[sub_expression[0]]   #"("
            num_stack=[]

            #当前"-"是负号而不是减号
            if(sub_expression[1]=="-"):
                sub_expression="(0"+sub_expression[1:]



            index=1

            while(sub_expression[index] != ")"):
                if(sub_expression[index].isdigit()):
                    num_str=sub_expression[index]
                    while(sub_expression[index + 1].isdigit()):
                        index+=1
                        num_str+=sub_expression[index]
                    num=(int)(num_str)
                    num_stack.append(num)
                    index+=1
                    continue
                #如果是操作符
                else:

                    if(sub_expression[index]=="-"):
                        #该"-"是负号
                        if(not sub_expression[index-1].isdigit()):
                            num_str = sub_expression[index]
                            while (sub_expression[index + 1].isdigit()):
                                index += 1
                                num_str += sub_expression[index]
                            num = (int)(num_str)
                            num_stack.append(num)
                            index += 1
                            continue

                    op_top=op_stack[-1]
                    if(op_map[sub_expression[index]]>op_map[op_top]):
                        op_stack.append(sub_expression[index])
                    else:
                        #4*5*3+2
                        #0-4*5-6
                        while(op_map[sub_expression[index]] <=op_map[op_top]):
                            op=op_stack.pop()
                            num_right=num_stack.pop()
                            num_left=num_stack.pop()
                            ans=get_ans(num_left,num_right,op)
                            num_stack.append(ans)
                            op_top = op_stack[-1]
                        op_stack.append(sub_expression[index])


                    index+=1
            while(len(op_stack)>1):#除了(还有别的操作符
                num_right=num_stack.pop()
                num_left=num_stack.pop()
                op=op_stack.pop()
                ans=get_ans(num_left,num_right,op)
                num_stack.append(ans)

            return num_stack[0]





            pass
        expression= "(" + expression + ")"
        stack=[]
        for ch in expression:
            if(ch=="("):
                stack.append(ch)
            elif(ch==")"):
                sub=stack.pop()
                sub+=")"
                temp=calc_sub(sub)
                if(stack==[]):
                    return temp
                stack[-1]+=(str)(temp)
            else:
                stack[-1]+=ch

while True:
    expression=input("input:")
    print(Calculator.calc(expression))

#0+1-2   0-1+2

