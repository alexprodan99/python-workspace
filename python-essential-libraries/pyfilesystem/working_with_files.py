from fs.osfs import OSFS
from fs.zipfs import ZipFS


# open a local files system for current directory
with OSFS('.') as myfs:
    if not myfs.exists('testdir'):
        myfs.makedir('testdir')
    with myfs.open('testdir/samplefile.txt', mode='w') as f:
        f.write('some text')
    with myfs.open('testdir/samplefile.txt', mode='r') as f:
        text = f.read()
        print(text)
    info = myfs.getinfo('testdir/samplefile.txt', namespaces=['details'])
    print(info.name)
    print(info.is_dir)
    print(info.size)
    print(info.type)
    print(info.modified)
    

# try to open and read a zip file
with ZipFS('ex.zip') as thezip:
    if thezip.exists('file1.txt'):
        with thezip.open('file1.txt', mode='r') as f:
            content = f.read()
            print(content)

    