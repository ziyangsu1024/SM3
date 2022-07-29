import random
import math

IV ='7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e'
T=[int('79cc4519',16)]*16+[int('7a879d8a',16)]*48
#print(Tj)
def ivfun(IV):
    res=[]
    for i in range(8):
        temp=int(IV[i*8:i*8+8],16)
        res.append(temp)
    return res
IV=ivfun(IV)
#print(IV)

def FFj(x,y,z,j):#输入应为10进制
    if j>=0 and j<=15:
        ff=x^y^z
    elif j>=16 and j<=63:
        ff=(x&y)|(x&z)|(y&z)
   # print(ff)
    return ff
#FFj(123333,1,12,1)
def GGj(x,y,z,j):#输入十进制
    if 0<=j<=15:
        gg=x^y^z
    else:                       #elifgaidiao
        gg=(x&y)|((~x)&z)
    return gg

def shift_left(x,num):#输入十进制输出十进制,循环左移
    y=str(bin(x))[2:].zfill(32)
    res=y[num:]+y[:num]
    return int(res,2)
    
#x=shift_left(1,2)
#print(x)
#print(int(x,2))
def sub_p0(x):#输入十进制,置换P0(X) = X ⊕ (X ≪ 9) ⊕ (X ≪ 17) 
    p0=int(bin(x^(shift_left(x,9))^(shift_left(x,17)))[2:].zfill(32)[-32:],2)
    return p0

def sub_p1(x):# 输入十进制,输出十进制P1(X) = X ⊕ (X ≪ 15) ⊕ (X ≪ 23
    p1=int(bin(x^(shift_left(x,15))^(shift_left(x,23)))[2:].zfill(32)[-32:],2)
    return p1

#m=shift_left(12,1)
#pint(bin(IV[0]))
#print(type(m))

def cf(vi,bi,j):#B是01字符串列表,IV是十进制列表
    reg=['']*8#8个字寄存器abcdefgh
    for i in range(8):
        reg[i]=vi[i]#则中间变量要以列表形式传递
    #print(reg)
    temp1=int(bin(shift_left(reg[0],12)+reg[4]+shift_left(T[j],j))[2:].zfill(32)[-32:],2)
    ss1=shift_left(temp1,7)
    temp2=bin(ss1^shift_left(reg[0],12))[2:].zfill(32)[-32:]
    ss2=int(temp2,2)
    temp3=bin(FFj(reg[0],reg[1],reg[2],j)+reg[3]+ss2+Ww[j])[2:].zfill(32)[-32:]
    tt1=int(temp3,2)
    tt2=int(bin(GGj(reg[4],reg[5],reg[6],j)+reg[7]+ss1+W[j])[2:].zfill(32)[-32:],2)
    reg[3]=reg[2]
    reg[2]=shift_left(reg[1],9)
    reg[1]=reg[0]
    reg[0]=tt1
    reg[7]=reg[6]
    reg[6]=shift_left(reg[5],19)
    reg[5]=reg[4]
    reg[4]=sub_p0(tt2)
   # res=([str[reg[i] for i in range(8)]reg[0]+reg[1]+reg[2]+reg[3]+reg[4]+reg[5]+reg[6]+reg[7])^vi
   # print(reg)
    return reg

B=[]
W=[]
Ww=[]
V=[]


def hash_fun(mess):#填充，迭代  算Wj和Wj撇（Wjj）
    m=bin(int(mess,16))[2:].zfill(4*len(mess))
    l=len(m)
   # print(m)
    k=0
    while(l+1+k)%512!=448:
        k+=1
    m+='1'+'0'*k+bin(l)[2:].zfill(64)
    #print(m)
    n=(l+k+65)//512
    #print(n)
    for i in range(n):
        B.append(m[i*512:i*512+512])
    #print(B)
    for i in range(n):
        for j in range(68):
            if 0<=j<=15:
                W.append(int(B[i][j*32:j*32+32],2))
                #print(W)
            else:
#^必须用于int
                temp=sub_p1(W[j-16]^W[j-9]^shift_left(W[j-3],15))
                tempp=temp^shift_left(W[j-13],7)^W[j-6]
                W.append(tempp)
        #print(W)    
        #print(len(W))        
        for j in range(64):
            Ww.append(W[j]^W[j+4])
        #print(Ww)
        V=IV
        for j in range(64):
            V=cf(V,B,j)
        V2=[bin(V[i])[2:].zfill(32) for i in range(8)]
       # print(V2)
        IV2=[bin(IV[i])[2:].zfill(32) for i in range(8)]
    
        res=int(V2[0]+V2[1]+V2[2]+V2[3]+V2[4]+V2[5]+V2[6]+V2[7],2)^int(IV2[0]+IV2[1]+IV2[2]+IV2[3]+IV2[4]+IV2[5]+IV2[6]+IV2[7],2)
    return bin(res)[2:].zfill(256)
        
            
if __name__ == '__main__':
    message='12345'
    m=hash_fun(message)
    print("杂凑值为",m)















    
