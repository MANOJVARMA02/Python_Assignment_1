try:
    def Test(arr,si,ci,inc):
        if(si==len(arr) and ci==0 and inc!=len(arr)):
            return "Balanced parenthesis"
        elif(si==len(arr) and ci!=0):
            return "UnBalanced parenthesis"
        elif(ci<0):
            return "Wrongly entered closing parenthesis before opening parenthesis"
        elif(arr[si]=="("):
            return Test(arr,si+1,ci+1,inc)
        elif(arr[si]==")"):
            return Test(arr,si+1,ci-1,inc)
        elif(arr[si]!="(" or arr[si]!=")"):
            return Test(arr,si+1,ci,inc+1)
    
    def main():
        arr=[i for i in input("Enter the list with  opening and closing parenthesis : ")]
        si=ci=inc=0
        print(Test(arr,si,ci,inc))
    
    main()
except:
    print("No parenthesis in input given")