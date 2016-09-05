def a(time):
    (hour,min,sec)=time.split(':')
    #rank = int(hour)
    rank = int(hour)*6+int(min)/10+1

    return int(rank)

print(a("00:10:00"))