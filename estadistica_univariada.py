import math
def promedio(lista):
    """
    calcula el promedio de una lista.
    
    parametros:
    -------------
    lista: lista de variables aleatorias
    
    retorna:
    ------------
    promedio : float
    """
    
    vals_in= []
    for v in lista:
        if math.isfinite(v):
            vals_in.append(v)
        
    promedio=sum(vals_in)/len(vals_in)
    return promedio
    
def mediana(vals_in):
    #se eliminan valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
#ordenar la lista
vals.sort()

if len(vals)% !=0:
    k= len(vals)//2
    mediana= vals[k]            
else: 
    k= len(vals)//2 
    mediana= (vals[k-1]+ vals[k])
return mediana

  

