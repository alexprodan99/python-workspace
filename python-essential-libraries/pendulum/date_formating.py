import pendulum

def main():
    dt = pendulum.datetime(2021, 12, 12)
    print(dt) # 2021-12-12T00:00:00+00:00
    
    print(dt.to_date_string()) # 2021-12-12
    print(dt.to_time_string()) # 00:00:00
    print(dt.to_datetime_string()) # 2021-12-12 00:00:00
    
    print(dt.to_formatted_date_string()) # Dec 12, 2021
    print(dt.to_day_datetime_string()) # Sun, Dec 12, 2021 12:00 AM
    
    print(dt.to_cookie_string()) # Sunday, 12-Dec-2021 00:00:00 UTC
    print(dt.to_iso8601_string()) # 2021-12-12T00:00:00Z
    print(dt.to_rfc822_string()) # Sun, 12 Dec 21 00:00:00 +0000
    
    
    
    print(dt.format("YYYY MM-DD HH:MM A")) # 2021 12-12 00:12 AM
    print(dt.format("dddd DD MMMM YYYY")) # Sunday 12 December 2021
    
    print(dt.format("YYYY MM-DD HH:MM A", locale="de")) # 2021 12-12 00:12 vorm.
    print(dt.format("dddd DD MMMM YYYY", locale="fr")) # dimanche 12 décembre 2021

    
    

if __name__ == '__main__':
    main()