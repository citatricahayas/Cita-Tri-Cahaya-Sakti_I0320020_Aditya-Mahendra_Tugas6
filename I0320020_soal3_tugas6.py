#Membuat Program Pengecekkan bilangan
#Input Data
s = 11
p = 24
print("===============PENGECEKKAN BILANGAN===============", "\n")
for num in range(s, p+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima")
                break
        else:
            print(num, "bilangan prima")