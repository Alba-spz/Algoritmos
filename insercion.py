def insertion_sort(arr):
    # Recorremos el array desde el segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Movemos los elementos del array que son mayores que la clave
        # una posición hacia adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Array original:", arr)
    insertion_sort(arr)
    print("Array ordenado:", arr)