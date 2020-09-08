def quick_sort(input_list):
    if (input_list is not None):
        size = len(input_list)
        if (size > 1):
            left = 0
            pivot = len(input_list) - 1
            aux_pivot = None
            aux_pivot_value = None
            while (left < pivot):
                left_value = input_list[left]
                pivot_value = input_list[pivot]
                if (left_value is None or pivot_value is None):
                    input_list = None
                    break
                else:
                    if (left_value < pivot_value):
                        if (pivot - left > 1):
                            aux_pivot = pivot - 1
                            aux_pivot_value = input_list[aux_pivot]
                            input_list[aux_pivot] = input_list[pivot]
                            input_list[pivot] = input_list[left]
                            input_list[left] = aux_pivot_value
                        else:
                            input_list[pivot] = left_value
                            input_list[left] = pivot_value
                        pivot-=1
                    else:
                        left+=1

                input_list = quick_sort(input_list[:pivot]) + [pivot_value] + quick_sort(input_list[pivot+1:]) 
        
    return input_list


def rearrange_digits(input_list):
    if (input_list is not None):
        max = ""
        min= ""
        
        sorted_list = quick_sort(input_list)
        size = len(sorted_list)
        if (size > 1):
            for index in range(0,size,2):
                max += str(sorted_list[index])
                if (index+1 < size):
                    min += str(sorted_list[index+1])
    
        elif (size == 1):
            max = input_list[0]
            min = input_list[0]

        return [max,min]
    
    return None




