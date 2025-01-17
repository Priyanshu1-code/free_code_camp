import numpy as np

#checking weather the input contains the required number.
def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
      
    #shaping the input list into matrix.
    matrix = np.array(input_list).reshape((3, 3))
  
    #calculation the output.
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return calculations

def get_user_input():
    try:
        user_input = input("Enter 9 numbers separated by spaces: ")
        input_list = list(map(int, user_input.split()))
        result = calculate(input_list)
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(e)


get_user_input()
