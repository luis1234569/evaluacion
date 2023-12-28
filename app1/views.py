from django.shortcuts import render

# Create your views here.
def mi_funcion (request):
    
    tupla = tuple(range(10))
    lista = list(range(10))
    lista[3] = 499
    del lista[3]
    lista[-1] = 1

    lista.sort(reverse=True)
    lista.pop()
    lista.pop(6)
    lis2 = [9, 9, 9]
    lista.append(lis2)
    lista.extend(lis2)
    lista = lista+lis2
    lista.extend(tupla)
    lista.insert(6, 27)
    # del lista[5:12]
    lista.remove(0)
    print(lista.index(1))
    print(tupla)
    lista[5:12] = tupla
    print(len(lista))
    lista = lista*3
    lista = [n**2 for n in lista]
    lista = [n**2 for n in lista if n % 3 == 0]
    lista = [str(n) for n in lista]
    
    
    
    diccionario={
        'none':1,
        'nondde':1,
        'nodne':1,
        'nonddde':1
    }
    
    diccionario['none'] = 223423
    # del diccionario['none']
    # valor=diccionario.pop('none')
    # diccionario.popitem()
    valor = diccionario.get('nongdtge', 'gdgd')
    diccionario['jose']= list(diccionario.keys())
    valor= diccionario.copy()
    nuevo_diccionario = {clave+'5': valor for clave, valor in valor.items() if valor is not None}

    diccionario.update(nuevo_diccionario)
    print(valor)
    
    claves = ['a', 'b', 'c']
    valor_predeterminado = 'mimom'
    nuevo_diccionario2 = dict.fromkeys(claves, valor_predeterminado)
    # Resultado: {'a': 0, 'b': 0, 'c': 0}
    diccionario.update(nuevo_diccionario2)



    teralista1= ['luis','juan','eduardo']
    teralista2= [1,2,3]
    i=0
    teralista3={}
    # for x, n in teralista3, teralista2:
    #     teralista3[x]= n
    for x in teralista1:
        print(i)
        teralista3[x]= teralista2[i]
        i+=1
    
    print(teralista3) 
    context={
        'diccionarioEvaluate': teralista3,
        'lista': lista,
        'diccionario': diccionario
    }
    
    return render(request, 'index.html', context)