import os
os.system('cls')
# os.system('clear')


print("os.path.dirname")
print(os.path.dirname(r'D:\Songs\English\On My Way.mp3'))
print("*"*25)


print("os.path.exists")
print(os.path.exists(r'D:\Songs\English\On My Way.mp3'))
print(os.path.exists(r'D:\Songs\English\fake.py'))


print("#"*25)
print("os.path.isfile")
print(os.path.isfile(r'D:\Songs\English\On My Way.mp3'))
print(os.path.isfile(r'D:\Songs\On My Way.mp3'))


print("*"*25)
print("os.path.isdir")
print(os.path.isdir(r'D:\Songs\English\On My Way.mp3'))
print(os.path.isdir(r'D:\Songs\English'))


print("#"*25)
print("os.path.join")
print(os.path.join(r'D:\Songs\English',  'On My Way.mp3'))

os.system('cls')
print("*"*25)
print("os.path.split")
print(os.path.split(r'D:\Songs\English\On My Way.mp3'))
print(os.path.split(r'D:\Songs\English'))
print(os.path.split(r'D:\Songs'))
print(os.path.split(r'D:'))

print("#"*25)
print("os.path.split")
dirname, fname = os.path.split(r'D:\Songs\English\On My Way.mp3')
print(dirname)
print(fname)

exit()
