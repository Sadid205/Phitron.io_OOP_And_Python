def multiply(**multiple):
    multiply_by_values=1
    for key,value in multiple.items():
        multiply_by_values=multiply_by_values*value
        print(f"{key}:{value}")
    print(f"first value is:{ multiple['first']}")
    return multiply_by_values

multi =  multiply(first=4,second=5,third=7,fourth=9)
print(multi)
