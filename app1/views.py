from django.shortcuts import render

# Create your views here.
def mi_funcion (request):
    lista1= ['luis','juan','eduardo']
    lista2= [1,2,3]
    i=0
    lista3={}
    # for x, n in lista3, lista2:
    #     lista3[x]= n
    for x in lista1:
        print(i)
        lista3[x]= lista2[i]
        i+=1
    
    print(lista3) 
    context={
        'diccionario': lista3
    }
    
    return render(request, 'index.html', context)