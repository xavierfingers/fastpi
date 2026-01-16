from mpmath import mp
def pi_dig(x, d):
     summed = mp.mpf(0)
     mp.dps = d
     for i in range(d + 1):
         t1 = mp.mpf(4/(8*i+1))
         t2 = mp.mpf(2/(8*i+4))
         t3 = mp.mpf(1/(8*i+5))
         t4 = mp.mpf(1/(8*i+6))
         summed += mp.mpf(1/16**i*(t1-t2-t3-t4))
         print(summed)
         with open("pi.txt", "w") as f:
          f.write(summed)
         
print("Welcome to FastPI!")
d = int(input("Enter digits: "))
pi_dig(1, d)