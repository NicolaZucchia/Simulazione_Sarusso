
numero = 3
lista_prova = [2]
lista_prova2 = [2, 2, 2]

class ExamException(Exception):
    pass

def differenza(a, b):
    try:
        return b-a
    except ValueError:
        raise ExamException('Sono stati inseriti uno o più valori non numerici')


class Diff(object):

    def __init__(self, ratio = 1):
        
        if ratio <= 0:
            raise ExamException("E' stato inserito un valore non accettabile per il ratio! ")
        self.ratio = ratio # valore di default

        

    def compute(self, lista):

        if type(lista) != list:
            raise ExamException("Non è stata inserita una lista! ")

        if len(lista) == 1:
            raise ExamException("La lista non può avere un solo elemento! ")

        for element in lista:
            try:
               int(element)
            except ValueError:
                raise ExamException("La lista presenta elementi non interi! ")

        lista_finale = []

        for i in range(1, len(lista)):
            k = differenza(lista[i-1], lista[i])
            lista_finale.append(k)
            
        for i in range(1, len(lista_finale)):
            lista_finale[i] = lista_finale[i] / self.ratio

        return lista_finale

'''
diff = Diff()
prova = input("Input della Diff: ")
result = diff.compute(lista_prova2)
print(result)
'''