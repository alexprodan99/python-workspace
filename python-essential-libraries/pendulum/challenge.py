import pendulum

def main():
    # dt1 = pendulum.datetime(2020, 4, 2)
    dt1 = pendulum.now()
    dt2 = pendulum.datetime(2020, 2, 7)
    
    print(f"Today is {dt1.format('dddd, MMMM Do')}")
    print(f"International Clash day is {dt2.format('dddd, MMMM Do')}")
    if (dt2 < dt1):
        print(f"International Clash day weny by {dt1.diff(dt2).in_days()} days ago")

if __name__ == '__main__':
    main()
