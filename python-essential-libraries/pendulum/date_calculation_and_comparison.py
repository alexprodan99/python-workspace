import pendulum

def main():
    dt1 = pendulum.datetime(2021,11,11,23,0,0)
    dt2 = pendulum.datetime(2021,12,12)
    
    print(dt1.to_date_string()) # 2021-11-11
    print(dt2.to_date_string()) # 2021-12-12
    
    newdate = dt1.add(hours=1)
    print(newdate.to_date_string())
    newdate = dt1.add(minutes=60)
    print(newdate.to_date_string())
    
    
    dt1 = dt1.add(years=2, months=3)
    print(dt1.to_date_string())
    dt1 = dt1.subtract(years=2, months=3)
    print(dt1.to_date_string())
    
    dt1 = dt1.add(years=-1, months=-4)
    print(dt1.to_date_string())
    
    
    print(dt1.is_past()) # True
    print(dt1.is_future())
    print(dt1.is_dst())
    
    print(dt1.is_leap_year())
    
    # dt1 is after dt2
    print(dt1 > dt2)
    print(dt1 < dt2)
    dt3 = pendulum.datetime(2021,12,12)
    print(dt2 == dt3)
    
    
    p = dt1.diff(dt2)
    
    print(p.in_days())
    print(p.in_hours())
    print(p.in_months())
    
    p = dt2.diff_for_humans(dt1) # 1 year after
    print(p)
if __name__ == '__main__':
    main()