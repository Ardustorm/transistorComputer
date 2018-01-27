VDD=5
GRND=0
ERROR=VDD/2
CHECKSTART=.0005
CHECKSTEP=.001


def bool(A):
    return A>=(VDD-ERROR)

def XOR(A,B):
    return (A and not B )or (B and not A)
    
def HA_S(A,B):
    return XOR(A,B)
def HA_C(A,B):
    return A and B
def FA_S(A,B,C):
    return XOR(C,XOR(A,B))
def FA_C(A,B,C):
    return (A and B) or (A and C) or (B and C)
    
def RCA(nums):
    bools=[]
    S=[False]*4
    for i in range(1,len(nums)):
        bools.append(bool(float(nums[i])))
    S[0]=HA_S(bools[0],bools[4])
    S[1]=FA_S(bools[1],bools[5],HA_C(bools[0],bools[4]))
    S[2]=FA_S(bools[2],bools[6],FA_C(bools[1],bools[5],HA_C(bools[0],bools[4])))
    S[3]=FA_S(bools[3],bools[7],FA_C(bools[2],bools[6],FA_C(bools[1],bools[5],HA_C(bools[0],bools[4]))))
    C=FA_C(bools[3],bools[7],FA_C(bools[2],bools[6],FA_C(bools[1],bools[5],HA_C(bools[0],bools[4]))))
    
    return C==bools[8] and S[0]==bools[9] and S[1]==bools[10] and S[2]==bools[11] and S[3]==bools[12]
    

def main():
    nextCheck=CHECKSTART
    all=True
    
    f = open("Test_RCA[4].txt","r")
    for line in f:
        nums = line.split()
        try:
            time = float(nums[0])
            if(time>nextCheck):
                nextCheck+=CHECKSTEP
                if(RCA(nums)):
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