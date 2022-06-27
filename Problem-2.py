def main():
    a=int(input("Enter the number : "))
    lst=[]
    if(a==0):
        print("Every number is factor of zero")
    else:
        for i in range(-abs(a),abs(a)+1):
            if(i!=0 and a%i==0):
                lst.append(i)
        print("The divisors are : ",lst)
        
main()
