def days_between_year( y1 , y2 ):
    """
    calculates days between two year excluding the years
    """
    d = 0

    for i in range ( y1 + 1 , y2 ):
        if i % 4 == 0 and ( i % 100 != 0 or i % 400 == 0 ):     #condition for leap year
            d += 366

        else:
            d += 365

    return d

def days_after_month(day,m1,y):
    """
    calculetes days after the date of month
    """
    d = 0

    month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    month2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}   # For leap year
    
    # calculate days left in the month
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 == 0 ):    
        d += month2[m1] - day          
    
    else:
        d += month[m1] - day
    
    #adds days from rest of months
    for i in range( m1 + 1 , 13 ):
    
        if y % 4 == 0 and ( y % 100 != 0 or y % 400 == 0 ):
            d += month2[i]
    
        else:
            d += month[i]
    
    return d

def days_before_month( day , m1 , y ):
    """
    calculates days before month
    """
    d = 0
    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    month2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}    #For leap year 
    d += day  # add no of days of month

    # adds days month before the given month 
    for i in range( 1 , m1 ):
        
        if y%4 and ( y % 100 != 0 or y % 400 == 0 ):
            d+=month2[i]
        
        else:
            d+=month[i]
    
    return d

def ifleapyear(year):
    if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ):
        return True
    return False

d1, m1, y1 = list ( map ( int, input( "date1 month1 year1: " ).split("/") ) )
d2, m2, y2 = list( map( int, input( "date2 month2 year2: " ).split("/") ) )                                                               
days = 0
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} 
if y1==y2:
    if m1!=m2:
        if ifleapyear(y1):
            for i in range(m1+1,m2):
                days += month2[i]
            days += month2[m1] - d1
            days += d2
        else:
            for i in range(m1 + 1, m2):
                days += month[i]
            days += month[m1] - d1
            days += d2
    else:
        days += d2 - d1
else:
    yd = days_between_year( y1 , y2 )
    mdb = days_before_month( d2 , m2 , y2)
    mda = days_after_month( d1 ,m1 , y1 )
    days = yd + mdb + mda
print("person survived", days, "days")