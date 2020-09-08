def sqrt(number):

    root = None
    floor_value = 0
    ceiling_value = number
    middle_value = None
    squared_number = None

    if (number == 0):
        return 0

    if (number <= 2):
        return 1

    while (True):
        middle_value = (floor_value + ceiling_value) // 2

        squared_number = middle_value * middle_value

        if (squared_number == number):
            root = middle_value
            break

        if (squared_number < number):
              floor_value = middle_value
              if (root is None):
                  root = middle_value
              else:
                  if (middle_value > root):
                      root = middle_value

        elif (squared_number > ceiling_value):
              ceiling_value = middle_value
        
        if (middle_value == floor_value + 1 or middle_value == ceiling_value - 1):
            break

    return root
    pass
