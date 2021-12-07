#1901ME39
#MANOJ KUMAR MADUGULA

import os
import shutil
import re

source =os.path.join(os.getcwd(),"wrong_srt")
temp = os.path.join(os.getcwd(),"temp_srt")
destination = os.path.join(os.getcwd(),"correct_srt")

if not os.path.exists(destination):
    os.makedirs(destination)

if os.path.exists(temp):
    shutil.rmtree(temp)

shutil.copytree(src=source ,dst= temp)
print(os.getcwd())

def renamer(wn,sp,ep):
    if wn ==1 :
        wn = 'Breaking Bad'
        current_dir = os.path.join(temp,wn)
        final_destination = os.path.join(destination,wn)
        if not os.path.exists(final_destination):
            os.makedirs(final_destination)
        shutil.rmtree(final_destination)
        if not os.path.exists(final_destination):
            os.makedirs(final_destination)

        os.chdir(current_dir)

        files = os.listdir()
        # print(files,type(files))
        for file in files :
            flis =file.split('.')
            f_ext = flis[-1]
            # print(f_ext)
            text =file
            pattern = re.compile(r'\d+')
            found = re.findall(pattern, text)
            num_lis=[]
            # print(type(found))
            if found:
                # print(found)
                for num in found :
                    num_lis.append(str(int(num)))
            # print(num_lis)
            sn = num_lis[0]
            en = num_lis[1]
            new_name = wn + "- Season "+sn.zfill(sp) +" Episode "+en.zfill(ep)+"."+f_ext
            # print(os.getcwd())
            # print(os.listdir())

            os.rename(file,os.path.join(final_destination,new_name))
            # print(temp)
            # print(source)1
    elif wn == 2 or wn == 3:
        if wn==2:
            wn='Game of Thrones'
        else :
            wn ="Lucifer"
        current_dir = os.path.join(temp, wn)
        final_destination = os.path.join(destination, wn)
        final_temp = os.path.join(temp, wn)

        if not os.path.exists(final_destination):
            os.makedirs(final_destination)
        shutil.rmtree(final_destination)
        if not os.path.exists(final_destination):
            os.makedirs(final_destination)

        os.chdir(current_dir)
        files = os.listdir()
        # print(files,type(files))
        for file in files:
            flis = file.split('.')
            f_ext = flis[-1]
            # print(f_ext)

            text_0 = file
            tlist = text_0.split('.')
            # print(tlist)
            tlist = tlist[0].split('-')
            # print(tlist[-1])
            episode_name = tlist[-1]

            text = file
            pattern = re.compile(r'\d+')
            found = re.findall(pattern, text)
            num_lis = []
            # print(type(found))
            if found:
                # print(found)
                for num in found:
                    num_lis.append(str(int(num)))
                # print(f'There are {len(found)} numbers')
            # print(num_lis)
            sn = num_lis[0]
            en = num_lis[1]
            new_name = wn + " - Season " + sn.zfill(sp) + " Episode " + en.zfill(ep) + " - " +episode_name+ "." + f_ext
            # print(os.getcwd())
            os.rename(file, os.path.join(final_destination, new_name))

        return

def regex_renamer():

    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))
    renamer(webseries_num , season_padding,episode_padding)
regex_renamer()
