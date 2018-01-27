VDD=5
GRND=0
ERROR=VDD/2
CHECKSTART=.0005
CHECKSTEP=.001


def bool(A):
    return A>=(VDD-ERROR)

def NAND(A,B,C):
    A = bool(float(A))
    B = bool(float(B))
    C = bool(float(C))
    return (not(A and B))==C

def main():
    nextCheck=CHECKSTART
    all=True
    
    f = open("Test_NAND.txt","r")
    for line in f:
        nums = line.split()
        try:
            time = float(nums[0])
            if(time>nextCheck):
                nextCheck+=CHECKSTEP
                if(NAND(nums[1],nums[2],nums[5])):
                    print("Time: "+nums[0]+"\nGOOD\n")
                else:
                    print("Time: "+nums[0]+"\nBAD\n")
                    print(line)
                    all = False
        except ValueError:
            pass
    f.close()
    print("All: "+str(all))
    
   





if __name__ == "__main__": main()   