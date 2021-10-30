a=[]

def Quick_Sort(low,high):
    if(low>=high):
        return
    else:
        p=Partition(low, high)        
        Quick_Sort(low,p)
        Quick_Sort(p+1,high)

def Partition(low, high):
    s=a[low]
    i,j=low+1,high-1
    done=False
    while(not done):
        while (i<=j) and (a[i]<=p): 
            i+=1
        while (j>=i) and (a[j]>=p):
            j-=1
        if (j < i):
            done=True
        else:
            a[i], a[j] = a[j], a[i]
    a[j], a[low] = a[low], a[j]
    return (j)



for i in range(0,10):
   a.append((int)(input("Enter number {y}th ".format(y= i))))
print(a)
Quick_Sort(0,len(a))
print(a)
