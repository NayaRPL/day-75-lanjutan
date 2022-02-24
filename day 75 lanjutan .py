def sortarray (a):
    for i in range (0,len(a)-2):
        for j in range (len(a)-1,i,-1):
            if a[j] < a[j-1]:
                # menukar elemen array 
                 a[j] , a[j-1] = a[j-1],a[j]
import array
B= array.array('i',[50,10,38,2,7,8])
print(B)
sortarray(B)
print(B)


                