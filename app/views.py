from django.shortcuts import render
from .forms import encriptarFor, descriptarFor

# Create your views here.

# def home(request):
# return render(request, 'app/home.html')


def home(request):
    data = {
        'formu': encriptarFor(),
        'form2': descriptarFor(),
    }
    if request.method == 'POST':
        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        formu1 = encriptarFor(data=request.POST)
        formu2 = descriptarFor(data=request.POST)

        if formu1.is_valid():
            matrizss = []
            pala = formu1.cleaned_data.get("palabra")
            palabra = pala.upper()
            llave = formu1.cleaned_data.get("llave")

            for p in range(len(palabra)):
                cont=0 #Este contador tiene funcion bandera, si el caracter de la cadena no se encuentra en el alfabeto este no sera cifrado
                for a in range(27):
                    if(palabra[p] == alfabeto[a]):
                        newPos = (a+llave) % 27
                        matrizss.append(alfabeto[newPos])
                        cont=1 ##Quiere decir que el caracter si se encuentra en el alfabeto
                if(cont==0):
                    matrizss.append(palabra[p])

            palCode = "".join(matrizss)

            data['mensaje'] = palCode

        if formu2.is_valid():
            matrizss = []
            pala2 = formu2.cleaned_data.get("mensaje")
            mensaje = pala2.upper()
            clave = formu2.cleaned_data.get("llave")

            for p in range(len(mensaje)):
                cont=0
                for a in range(27):
                    if(mensaje[p] == alfabeto[a]):
                        newPos = (a-clave) % 27
                        matrizss.append(alfabeto[newPos])
                        cont=1 
                if(cont==0):
                    matrizss.append(mensaje[p])


            palCode2 = "".join(matrizss)

            data['mensaje2'] = palCode2

    return render(request, 'app/home.html', data)
