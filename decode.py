import os
import zlib

PATH_BASE = os.getcwd() + '/stock-history/'
PATH_COMPRESSED = PATH_BASE + 'compressed/'
PATH_DECOMPRESSED = PATH_BASE + 'decompressed/'

print('Check Paths:\n' + '\tBASE PATH: ' + PATH_BASE + '\n\tCOMPRESSED PATH: ' + PATH_COMPRESSED + '\n\tDECOMPRESSED PATH: ' + PATH_DECOMPRESSED)

print('Processing Dir:')
for dir in sorted(os.listdir(PATH_COMPRESSED)):
    print(dir)
    
    
    for file in [doc for doc in sorted(os.listdir(os.path.join(PATH_COMPRESSED, dir))) if doc.endswith('.txt')]:
        print('\t' + file)
            
        src_path = PATH_COMPRESSED + dir + '/' + file
        dest_path = PATH_DECOMPRESSED + dir + '/' + file

        with open(src_path, 'rb') as compressed_file:
            compressed_data = compressed_file.read()
            # print(compressed_data)

        decompressed_data = zlib.decompress(compressed_data)

        with open(dest_path, 'wb') as decompressed_file:
            decompressed_file.write(decompressed_data)
            