import os, re


if __name__ == '__main__':
    directory = 'C:\\Users\\inbon\\Downloads\\'
    filenames = os.listdir(directory)
    filename_pattern = re.compile(r'(_MINF[0-9]*_[0-9]*_)(.*)')
    for each_filename in filenames:
        if filename_components := filename_pattern.search(each_filename):
            print(directory + each_filename)
            print('==> ' + directory + filename_components.group(2))
            #os.rename(directory + each_filename, directory + filename_components.group(2))
