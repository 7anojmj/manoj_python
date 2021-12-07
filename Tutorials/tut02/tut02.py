#Manoj Kumar Madugular
#1901me39

# import os
# os.system('clear')

def get_memory_score(n):
    slis=[]
    score = 0
    for i in range(len(n)):
        if(len(slis)<5):
            if n[i] in slis:
                score+=1
            else:
                slis.append(n[i])
        else:
            if (n[i] in slis):
                score+=1
            else:
                slis.pop(0)
                slis.append(n[i])
                
    # print(slis)   
    # print(n)
    return score
# input_nums = [1,4, "a", 3, 5, "Star", 7.5]
input_nums = [3, 4, 1, 6, 3, 3, 9, 0, 0, 0 ]
number_list=[]
word_list=[]
x=int(1.0)
# print(type(x))

for i in range(0,len(input_nums)):
    if type(input_nums[i])==type(x) :
        number_list.append(input_nums[i])
    else:
        word_list.append(input_nums[i])
# print("this is number list",number_list)
# print("this is word list ", word_list)
if (len(word_list)>=1):
    print("Please enter a valid input list . Invalid inputs detected : ",word_list )
else:
    # print('all is well')
    print("Score : ",get_memory_score(number_list))
    

        
