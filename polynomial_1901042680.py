def polynomial(coefficients, x):
    result = 0
    exponent = len(coefficients)-1
    for i in coefficients:
        temp = pow(x,exponent)
        result += i * temp
        exponent -= 1
        
    print("The result is: ", result)
    
polynomial([0,1,3,2],4)
