def selection_sort(arr):
    # Recorre todo el arreglo
    for i in range(len(arr)):
        # Encuentra el elemento mínimo en el arreglo no ordenado
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Intercambia el elemento mínimo con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Arreglo original:", arr)
    selection_sort(arr)
    print("Arreglo ordenado:", arr)