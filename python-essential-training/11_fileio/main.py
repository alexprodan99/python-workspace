def main():
    f = open("./lines.txt")
    for line in f:
        print(line.rstrip())
    
    # Text files
    # read text (t)
    infile = open("./lines.txt", "rt")
    # it will create file if not exists
    outfile = open("./lines_copy.txt", "wt")
    
    for line in infile:
        print(line.rstrip(), file=outfile)
        # flush = True so that we will print dots just when we will meet a \n (see last print statement with done)
        print(".", end="", flush=True)
    outfile.close()
    print("\n Done")
    
    # to point again to the start of the file
    infile = open("./lines.txt", "rt")
    outfile = open("./lines_copy.txt", "wt")
    
    for line in infile:
        outfile.writelines(line)
        # flush = True so that we will print dots just when we will meet a \n (see last print statement with done)
        print(".", end="", flush=True)
    outfile.close()
    
    print("\n Done")
    
    # Binary files
    infile = open("./market_cycles.PNG", "rb")
    outfile = open("./out_bin.jpg", "wb")
    while True:
        buf = infile.read(10240)
        
        if buf:
            outfile.write(buf)
            print(".", end="", flush=True)
        else:
            break
    outfile.close()
    print("\n done")
    
    
    
if __name__ == '__main__':
    main()