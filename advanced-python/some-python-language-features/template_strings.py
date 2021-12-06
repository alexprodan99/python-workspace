from string import Template

def main():
    str1 = 'You are watching {0} by {1}'.format('Advanced Python', 'Apr')
    print(str1)
    # more secure this approach
    temp1 = Template('You are watching ${title} by ${author}')
    str2 = temp1.substitute(title='Advanced Python', author='Apr')
    
    print(str2)
    
    data = {
        'author': 'Apr',
        'title': 'Advanced Python'
    }
    str2 = temp1.substitute(**data)
    print(str2)
    str2 = temp1.substitute(data)
    print(str2)
    
    
if __name__ == '__main__':
    main()