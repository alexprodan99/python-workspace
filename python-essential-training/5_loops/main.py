def main():
    # for + while loop
    n = 0
    while n < 5:
        print(n)
        n += 1
    
    for i in range(n):
        print(i)
        
    # tuple of items
    items = ("sword", "arrow", "bow")
    for item in items:
        print(item)
        
    
    for item in items:
        if item == 'arrow':
            break
        print(item)
    for item in items:
        if item == 'sword':
            continue
        print(item)
    
        
    


if __name__ == '__main__':
    main()