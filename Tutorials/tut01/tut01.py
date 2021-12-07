# Manoj kumar madugula
#1901me39

count =0
def meraki_finder(num):
    # print("tada")
    global count
    num_num=[] #this list contains the numbers with in the numbers
    arb_num=num  #initilizing an arbitary number which is the same number given to the function 
    # print(arb_num)
    f_num =[] #this list contains all the numbers after separting and made difference
    #this while loop separates the numbers (247 will be seperated as 2,4,7)
    while(arb_num!=0):
        arb=arb_num%10
        num_num.append(arb)
        arb_num=arb_num-arb
        arb_num=arb_num/10
    # print("arb",arb,  "arb_num",arb_num)
    # print("tested")
    for i in range(len(num_num)-1):
        if abs(num_num[i]-num_num[i+1])==1 :
            # print("yes {0} is a meraki number ".format(num))
            f_num.append("yes")
        else:
            f_num.append("no")
    # print(f_num)
    if ("no" in f_num):
        print("No - {0} is not a Meraki number".format(num))
    else:
        print("Yes - {0} is a Meraki number".format(num))
        count = count+1
        
            
        
    # print(num_num)


def meraki_helper(n):
    # print(n[0])
    global count
    for i in range(len(n)):
        if n[i]>=0 and n[i]<10 :
            print("Yes - {0} is a Meraki number ".format(n[i]))   #if a number is grater than 9 then it passes to anothor function to 
            count = count+1                                       #to check whether the number is meraki or not 
        else:
            meraki_finder(n[i])
    


input_list = [12,14,56,78,98,54,678,134,789,0,7,5,123,45,76345,987654321]
meraki_helper(input_list)
print("the input list contains {0} meraki and {1} non meraki numbers".format(count,len(input_list)-count))