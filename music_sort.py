import os, shutil, glob

files = glob.glob("*.mp3")
files.sort(key=os.path.getmtime)

source = input('Enter music folder to sort (/home/music/): ')

files = os.listdir(source)
for file_name in files:
    if ''.join(file_name[-3:]) == 'mp3':
        print(file_name)
        if len(file_name.split('-')) > 1:
            author_name = file_name.split('-')[0]
        else:
            author_name = '*Unknow*'
        try:
            os.mkdir(os.path.join(source, source + author_name))
        except FileExistsError:
            pass
        new_dir = source + author_name
        print(new_dir)
        shutil.move(source+file_name, new_dir+'/'+file_name)
