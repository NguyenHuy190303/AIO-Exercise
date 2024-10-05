import math

def is_number(n):
    # Hàm kiểm tra xem n có phải là số hay không (đã được cung cấp)
    try:
        float(n)
        return True
    except ValueError:
        return False

def activation_function(x, function_name):
    if not is_number(x):
        print("x must be a number")
        return

    x = float(x)
    alpha = 0.01

    if function_name == "sigmoid":
        return 1 / (1 + math.exp(-x))
    elif function_name == "relu":
        return max(0, x)
    elif function_name == "elu":
        return x if x > 0 else alpha * (math.exp(x) - 1)
    else:
        print(f"{function_name} is not supported")

# Ví dụ sử dụng:
while True:
    x = input("Input x = ")
    function_name = input("Input activation function (sigmoid | relu | elu): ")

    result = activation_function(x, function_name)
    if result is not None:
        print(f"{function_name}: f({x}) = {result}")
