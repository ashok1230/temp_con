class converter:
    def __init__(self):
	change="Enter f for fahrenheit to celsius change or c to celsius to Fahrenheit"
	ch=raw_input(change)
	choice=ch.lower()
        try:
            if choice=='f':
                for_heit=float(raw_input("enter fahrenheit temperature"))
                con=(for_heit-32.00)/1.8
                print con
            elif choice=='c':
                celsiu=float(raw_input("enter celsius temperature"))
                con=celsiu*1.8+32.00
                print con
            else:
                print 'You enter wrong choice'
        except ValueError:
            print 'You enter wrong input'

a=converter()

