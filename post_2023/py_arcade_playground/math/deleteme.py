def function(x, y):
    if x == 1:
        return y
    else:
        return y + function(x - 1, y)
    
result = function(5,5)

print(result)