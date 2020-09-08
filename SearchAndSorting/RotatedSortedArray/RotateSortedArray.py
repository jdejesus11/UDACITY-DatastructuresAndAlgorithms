def _is_a_peak(input_list,index):
    lower_boundary = 0
    higher_boundary = len(input_list) - 1
    value = input_list[index]
    if (index != lower_boundary and index != higher_boundary):
        return (input_list[index-1] < value  and value > input_list[index + 1])
         
    return False

def _is_a_floor(input_list,index):
    lower_boundary = 0
    higher_boundary = len(input_list) - 1
    value = input_list[index]
    if (index != lower_boundary and index != higher_boundary):
        return (input_list[index-1] > value  and value < input_list[index + 1])
         
    return False

 
def rotated_array_search(input_list, number):
    index = _rotated_array_search(input_list,number,0,len(input_list) - 1)
    return index
    pass


def _rotated_array_search(input_list,number,left,rigth):
   
   if (left < rigth):
       middle_index = (left + rigth ) // 2
       middle_value = input_list[middle_index]
       is_a_peak = _is_a_peak(input_list,middle_index)
       is_a_floor = _is_a_floor(input_list,middle_index)
       if (middle_value == number):
           return middle_index

       if (is_a_peak is False and is_a_floor is False):
            if (middle_value > number):
                return _rotated_array_search(input_list,number,left,middle_index)
            
            if (middle_value < number):
                return _rotated_array_search(input_list,number,middle_index+1,rigth)

       elif (is_a_peak is True or is_a_floor is True): 
            left_result  =  _rotated_array_search(input_list,number,left,middle_index)
            if (left_result != -1):
                return left_result
            rigth_result = _rotated_array_search(input_list,number,middle_index+1,rigth)
            if (rigth_result != -1):
                return rigth_result
    
   if (left == rigth):
       if (input_list[left] == number):
           return left
            

   return -1






