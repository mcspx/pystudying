__author__ = 'rpm'
while True :
    try :
        input=int(raw_input('Enter numbers please: '))
    except ValueError :
        print("Value error ))")
    else :
        print "Good number ", input
        print 'bye!'
        raise KeyboardInterrupt

