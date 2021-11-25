#!/usr/bin/env python3

# above is the shebang line => for unix systems (in this example env is used for getting path of python3)
# another way to write this line (hardcoded path to python)
#!/usr/local/bin/python3
import platform
# for getting operating system and python version details
print('hello world. We are on {} and python version is: {}'.format(platform.platform(), platform.python_version()))