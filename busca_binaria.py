def busca_binaria(array, value):
    if len(array) < 1:
        return -1
    
    begin = 0
    end = len(array) - 1
    
    while end >= begin:
        mid = (begin + end) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            end = mid - 1
        else:
            begin = mid + 1
        
    return -1
              