print("VDD VDD 0 5")
print("")

for i in range(9):
    print("VA[{}] A[{}] 0 PULSE(0 5 {}m 2n 1n {}m {}m)".format(i,i,2**i,2**i,2**(i+1)))

print("")

j=9
for i in range(9):
    print("VB[{}] B[{}] 0 PULSE(0 5 {}m 2n 1n {}m {}m)".format(i,i,2**j,2**j,2**(j+1)))
    j+=1
    