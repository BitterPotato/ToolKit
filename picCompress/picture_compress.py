import tinify
import sys
import os

def compress_pic(dirpath, filename):
  if '_c' not in filename:
    dirpath = dirpath + '\\'

    index = filename.find('.')
    target_filename = filename[:index] + '_c' + filename[index:]

    tinify.key = '_-xrtTumDq-1fkIUGnEQsNeTfhREU_jj'
    tinify.from_file(dirpath + filename).to_file(dirpath + target_filename)

    print(filename + ' has been compressed......')
    os.remove(dirpath + filename)

def compress_bypath(path):
  if os.path.isfile(path):
    compress_pic(os.path.dirname(path), os.path.basename(path))
  else:
    for filename in os.listdir(path):
      compress_bypath(path + '\\' + filename)

compress_bypath(sys.argv[1])