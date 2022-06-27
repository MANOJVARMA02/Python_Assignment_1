def main():
    pswd=input("Enter the password : ")
    b=c=d=e=f=0
    spl_chrtrs="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in range(len(pswd)):
        if(pswd[i]>='a' and  pswd[i]<='z'):
            c=c+1
        elif(pswd[i]>='A' and pswd[i]<='Z'):
            d=d+1
        elif(pswd[i]>='0' and pswd[i]<='9'):
            e=e+1
        elif(pswd[i] in spl_chrtrs):
            f=f+1
        if(i+1<len(pswd) and pswd[i]==pswd[i+1]):
            b=b+1
    if( b==0 and c>=1 and d>=1 and e>=1 and f>=1 and (len(pswd)>=8 and len(pswd)<=16)):
        print("Valid Password")
    else:
        print("Invalid password")
        
main()