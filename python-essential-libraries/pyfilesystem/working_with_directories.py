from fs.osfs import OSFS

# with OSFS('.') as myfs:
#     print(myfs.tree())
    
with OSFS('.') as myfs:
    # returns strings
    dirlist = myfs.listdir('testdir')
    print(dirlist)
    
with OSFS('.') as myfs:
    # returns objects
    dirlist =list(myfs.scandir('testdir'))
    print(dirlist)
    
with OSFS('.') as myfs:
    # returns objects
    dirlist =list(myfs.filterdir('testdir', files=['*.txt']))
    print(dirlist)
    
with OSFS('.') as myfs:
    # returns objects
    dirlist =list(myfs.scandir('testdir', namespaces=['details']))
    for info in dirlist:
        print(info.name, info.size)
        
with OSFS('.') as myfs:
    # copy dirs with all its files
    # create=True => if copy_test_dir is not existing then create it
    myfs.copydir('testdir', 'copy_test_dir', create=True)
    
    
with OSFS('.') as myfs:
    if (myfs.exists('copy_test_dir')):
        # myfs.removedir('copy_test_dir') -> it will throw error if directory contains any other file
        myfs.removetree('copy_test_dir')
    