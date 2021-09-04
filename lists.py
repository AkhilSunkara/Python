totalValue=0
count=0
while True:
    num=input('Enter a vaild number')
    if num == 'done':
        break
    float_value= float(num)
    totalValue = totalValue + float_value
    count = count + 1
avg = totalValue / count
print('Aveage of numbers : ', avg)

#Let get this program using lists 
#We will create a list name avg_list
avg_list=list()
while True :
    number = input('Enter the list of numbers: ')
    if number == 'done' :
        break
    temp_value = float(number)
    #.append() method is used to push values into list
    avg_list.append(temp_value)
#sum() and len() are functions in lists 
average = sum(avg_list)/len(avg_list)
print('List average: ', average)
