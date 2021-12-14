from fs.osfs import OSFS
from fs.zipfs import ZipFS


with OSFS('.') as myfs:
    print('--Files--')
    for path in myfs.walk.files():
        print(path)
    print('--Dirs--')
    for path in myfs.walk.dirs():
        print(path)
        
    print('--Filter files--')
    for path in myfs.walk.files(filter=['*.txt']):
        print(path)
    
with OSFS('.') as myfs:
    print('--Files + dirs Infos--')
    for path, info in myfs.walk.info(namespaces=['details']):
        print(path, info.is_dir, info.size)

with OSFS('.') as myfs:
    print('--Step walk()--')
    for step in myfs.walk():
        print(step.path, step.files, step.dirs)
        
with ZipFS('ex.zip') as thezip:
    print('--Walk zip--')
    for step in thezip.walk():
        print(step.path, step.files, step.dirs)