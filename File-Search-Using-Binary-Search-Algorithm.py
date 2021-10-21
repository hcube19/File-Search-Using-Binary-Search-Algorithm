import glob
import webbrowser as wb
import os

def binary_search(file_name, files):
    low = 0
    high = len(files) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if os.path.basename(files[mid]) == file_name:
            return mid
        elif os.path.basename(files[mid]) > file_name:
            high = mid - 1
        else:
            low = mid + 1


doc = []
directory = sorted(glob.glob("D:\\files\\*.pdf"))
for documents in directory:
    doc.append(documents)
print("Documents in the directory\n",doc)

img = []
directory = sorted(glob.glob("D:\\files\\*.png"))
for images in directory:
    img.append(images)
print("Images in the directory\n",img)

music = []
directory = sorted(glob.glob("D:\\files\\*.mp3"))
for musics in directory:
    music.append(musics)
print("Music in the directory\n",music)

mix = []
mix.append(doc)
mix.append(img)
mix.append(music)
file_type = int(input("Input 0 for Document \nInput 1 for Image\nInput 2 forMusic : "))
files = mix[file_type]
print("Files in selected list : ", files)
file_name = input("Enter the file name with extension : ")
index = input("Do User Know the position of file in List? (Y/N) : ")

if index == "N":
    result = binary_search(file_name, files)
    print("Position of file in list: ", result)
    wb.open_new(files[result])
    print("File Opened")
else :
    pos = int(input("Enter the Position in list : "))
    if os.path.basename(files[pos])==file_name:
        wb.open_new(mix[file_type][pos])
        print("File Opened")
    else:
        print("Wrong Position")