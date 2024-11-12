def pass_(n):
    result = []
    i = 1
    while i < (n - 1):
        j = 2
        while j < n:
            if i < j:
                if n % (i + j) == 0:
                    result.append(i)
                    result.append(j)
            j += 1
        i += 1
    return result
num_ = int(input("Введите число из первой вставки в диапазоне 3:20: "))
if num_ >2 and num_ < 21:
    print(pass_(num_))
else:
    print("Введено число вне диапазона 3:20")
