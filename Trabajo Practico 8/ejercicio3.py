def position(a,b,home=0):
    list=[]
    index=a.find(b,home)
    if index !=-1:
        list.append(index)
        list.extend(position(a,b,index +1))
    
        
    return list

a="Hola, como estas"
b="o"
print("El segundo string se encuentra en las posiciones: ",position(a,b) )