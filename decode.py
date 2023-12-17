import os
import zlib

PATH_BASE = os.getcwd() + '/stock-history/'
PATH_COMPRESSED = PATH_BASE + 'compressed/'
PATH_DECOMPRESSED = PATH_BASE + 'decompressed/'

print('Check Paths:\n' + '\tBASE PATH: ' + PATH_BASE + '\n\tCOMPRESSED PATH: ' + PATH_COMPRESSED + '\n\tDECOMPRESSED PATH: ' + PATH_DECOMPRESSED)

print('Processing Dir:')
for dir in sorted(os.listdir(PATH_COMPRESSED)):
    if os.path.isdir(PATH_COMPRESSED + dir) :
        print(dir)
        
        for file in sorted(os.listdir(os.path.join(PATH_COMPRESSED, dir))):
            print('  ' + file)
    
            src_path = PATH_COMPRESSED + dir + '/' + file
            dest_path = PATH_DECOMPRESSED + dir + '/' + file

            
            try:
                with open(src_path, 'rb') as compressed_file:
                    compressed_data = compressed_file.read()

                decompressed_data = zlib.decompress(compressed_data)

                with open(dest_path, 'wb') as decompressed_file:
                    decompressed_file.write(decompressed_data)

            except zlib.error as e:
                print(f"Error decompressing file {file}: {e}")
                