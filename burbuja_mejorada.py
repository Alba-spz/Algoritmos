def burbuja_mejorada(arr):
    n = len(arr)
    for i in range(n):
        # Bandera para detectar si hubo algún intercambio
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor
                # que el siguiente elemento
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Si no hubo intercambio, la lista ya está ordenada
        if not swapped:
            break
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Arreglo original:", arr)
    sorted_arr = burbuja_mejorada(arr)
    print("Arreglo ordenado:", sorted_arr)