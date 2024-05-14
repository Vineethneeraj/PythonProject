from performance import performance
@performance
def divisible_7():
    print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

