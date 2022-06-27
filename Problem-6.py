import datetime
try:
    def main():
        a=int(input("enter the day of DOB : "))
        b=int(input("enter the month of Dob in number : "))
        today=datetime.date.today();
        c=today.year
        dob=datetime.date(c,b,a)
        if(dob.day==29 and dob.month==2):
            rem= 4-(today.year%4)
        else:
            rem=1
        next_year=datetime.date((today.year)+rem,dob.month,dob.day)
        countdown=next_year-today;
        print(countdown.days)

    main()

except:
    print("Enter Valid Data")