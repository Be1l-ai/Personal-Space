def multiply(x):
    x = x * 5
    return x

def result():
     take =  int(input())
     i = 0
     while i < 5:
        multiply(take)
        i+=1
        print(take)
result()