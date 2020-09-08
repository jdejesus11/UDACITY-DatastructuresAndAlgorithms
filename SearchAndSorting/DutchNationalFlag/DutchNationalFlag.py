"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

Args:
    input_list(list): List to be sorted
"""
class DutchNationalFlag:

    def __init__(self, input_list):
        self.input_list = None
        self.sorted_input_list = None
        if (input_list is not None):
            self.input_list = input_list
            self.sorted_input_list = input_list.copy()

    def sort(self):
        if (self.sorted_input_list is not None):
            size = len(self.sorted_input_list)
            left_index = 0
            rigth_index = size - 1
            extra_index = None
            while (left_index < rigth_index):
                
                left_value = self.sorted_input_list[left_index]
                rigth_value = self.sorted_input_list[rigth_index]
                
                if (left_value == 0):
                    left_index+=1

                elif (left_value == 2):
                    if (rigth_value != 2):
                        self.sorted_input_list[left_index] = rigth_value
                        self.sorted_input_list[rigth_index] = left_value
                    rigth_index-=1
                    
                elif (left_value == 1):
                    if (rigth_value == 0):
                        self.sorted_input_list[left_index] = 0
                        self.sorted_input_list[rigth_index] = 1
                        left_index+=1
                        if (extra_index is not None):
                            rigth_index = extra_index
                            extra_index = None
                    else: 
                        if (rigth_value == 1 and extra_index is None):
                            extra_index = rigth_index
                        else:
                            if (rigth_value == 2 and extra_index is not None):
                                self.sorted_input_list[rigth_index] = self.sorted_input_list[extra_index]
                                self.sorted_input_list[extra_index] = rigth_value
                                rigth_index = extra_index + 1
                                extra_index = None
                        rigth_index-=1
                    
    def __repr__(self):
        string = None
        if (self.input_list is not None and self.sorted_input_list is not None):
            string = "Input:  "
            size = len(self.input_list) - 1
            if (size >= 0):
                for index, value in enumerate(self.input_list):
                    string+=str(value)
                    if (index != size):
                        string+= " "
            
                string+="\n\n"

                string+= "Output: "
                size = len(self.sorted_input_list) - 1
                for index, value in enumerate(self.sorted_input_list):
                    string+=str(value)
                    if (index != size):
                        string+= " "
                string+="\n"
            else:
                string = "No results"
        else:
            string = "No results"
        return string