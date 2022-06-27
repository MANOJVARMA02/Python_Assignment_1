try:
    def main():
        cube = float(input('Enter the number : '))
        epsilon = 0.01
        if(cube>-1 and cube<1):
            low = abs(cube)
            high = 1
        else:
            low=0
            high=abs(cube)
        guess = (high + low)/2.0
        while abs(guess**3 - abs(cube)) >= epsilon:
            if guess**3 < abs(cube) :
                low = guess
            else:
                high = guess
            guess = (high + low)/2.0
        if(cube>=0):
            print(guess, 'is close to the cube root of', cube)
        else:
            print(-guess, 'is close to the cube root of',cube)
        
    main()

except:
    print("Enter valid number")