def dayname(daynum):
    if daynum==0:
        return 'Sunday'
    elif daynum==1:
        return 'Monday'
    elif daynum==2:
        return 'Tuesday'
    elif daynum==3:
        return 'Wednesday'
    elif daynum==4:
        return 'Thursday'
    elif daynum==5:
        return 'Friday'
    elif daynum==6:
        return 'Saturday'
    else:
        return
    
def daynum(dayname):
    '''converts day to day number'''
    if dayname=='Sunday':
        return 0
    elif dayname=='Monday':
        return 1
    elif dayname=='Tuesday':
        return 2
    elif dayname=='Wednesday':
        return 3
    elif dayname=='Thursday':
        return 4
    elif dayname=='Friday':
        return 5
    elif dayname=='Saturday':
        return 6
    else:
        return

def dayadd(today, stay):
    result=(stay)%7
    answer=(result)+(daynum(today))
    return dayname(answer)

print(dayadd("Monday", 5))