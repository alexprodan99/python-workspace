from datetime import datetime
import time
import pendulum



def main():
    dt1 = pendulum.datetime(2020,7,28)
    print(dt1)
    
    print(isinstance(dt1,datetime)) # true => so basically is compatible with existing datetime from python
    print(dt1.timezone.name) # default is utc => so it's helpful and easy to work with dates
    
    # use a given timezone if you want
    dt2 = pendulum.datetime(2020,7,28, tz="America/New_York")
    print(dt2)
    
    # convert from one timezone to another
    dt3 = dt1.in_timezone('Europe/Paris')
    print(dt3)
    
    
    dt4 = pendulum.now()
    print(dt4)
    print(dt4.timezone.name) # Europe/Moscow in my case
    
    
    dt4 = pendulum.now("Europe/London")
    print(dt4)
    print(dt4.timezone.name)
    
    
    here = pendulum.local(2021,11, 11)
    print(here)
    print(here.timezone.name) # Europe/Moscow in my case
    
    
    # today, tomorrow, yesterday
    today = pendulum.today()
    tomorrow = pendulum.tomorrow()
    yesterday = pendulum.yesterday()
    
    print(today)
    print(tomorrow)
    print(yesterday)
    
    yesterday = pendulum.yesterday("America/New_York")
    print(yesterday)
    
    
    t = time.time()
    print(t)
    dt5 = pendulum.from_timestamp(t)
    print(dt5)
    print(dt5.timezone.name) # UTC
if __name__ == '__main__':
    main()