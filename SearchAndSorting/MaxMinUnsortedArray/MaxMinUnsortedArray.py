def get_min_max(input):
    if (input is not None):
            size = len(input)
            if (size > 0):
                left_index = 0
                rigth_index = len(input) - 1
                min_value = input[left_index]
                max_value = input[rigth_index]
                while (left_index <= rigth_index):
                    left_value = input[left_index]
                    rigth_value = input[rigth_index]
                    
                    if (left_value < min_value):
                        min_value = left_value
                    
                    elif (left_value > max_value):
                        max_value = left_value
                    

                    if (rigth_value < min_value):
                        min_value = rigth_value
                    
                    elif (rigth_value > max_value):
                        max_value = rigth_value
                    
                    left_index+=1
                    rigth_index-=1

                return (min_value,max_value)
    
    return None

result = get_min_max([0,0,0,0,0,0,0,0])
print(result)
