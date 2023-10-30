def more(arra,num,si):
    
    if si>0:
       
        if arra[si]>num:
            num=arra[si]
            print(arra[si])
            num=more( arra,num,si-1)
        else:
            num=more(arra,num,si-1)
    return num
  
       


number=0
list=[2,10,12,3,4,5,6,5]
size=len(list)
print("El número mas grande es :",more(list,number,size-1))