

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b) # b'ABCD'
    
    s = 'my string'
    print(s)
    
    # error
    # print(s+b)
    print(s + str(b)) # my stringb'ABCD'

    # but there is an extra b there and '' => use decode
    # convert bytes to string
    s2 = b.decode('utf-8')
    print(s + s2) # my stringABCD
    
    # convert string to bytes
    b2 = s.encode('utf-8')
    print(b + b2) # b'ABCDmy string'
    
    b3 = s.encode('utf-32')
    print(b3) # b'\xff\xfe\x00\x00m\x00\x00\x00y\x00\x00\x00 \x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'
    
if __name__ == '__main__':
    main()