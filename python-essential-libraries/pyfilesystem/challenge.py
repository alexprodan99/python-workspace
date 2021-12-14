# print total size of all files from a given directory (including subdirectories)
from fs.osfs import OSFS

with OSFS('.') as myfs:
    total = 0
    for path, info in myfs.walk.info(namespaces=['details']):
        if not info.is_dir:
            total += info.size
    print(f'Total size={total}')