a=[]

def Merge(left_list, right_list):
    i,j=0,0
    sorted_list=[]
    while(i < len(left_list))and(j<len(right_list)):
        if(left_list[i]<=right_list[j]):
            sorted_list.append(left_list[i]);i+=1
        else:
            sorted_list.append(right_list[j]);j+=1
    while(i<len(left_list)):
            sorted_list.append(left_list[i]);i+=1
    while(j<len(right_list)):
            sorted_list.append(right_list[j]);j+=1
                
    return sorted_list

def Merge_Sort(list):
    if(len(list)==1):# low=0,high=0 i.e. len=-1
        return list
    else:
        mid=len(list)//2
        return Merge(Merge_Sort(list[:mid]),Merge_Sort(list[mid:]))



#a=[34, 67, 8, 19, 2, 23, 1, 91]
for i in range(0,10):
    a.append((int)(input("Enter number {y}th ".format(y= i))))
print(a)
print(Merge_Sort(a))