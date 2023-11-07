import fitz  
import os

while True:
    print("PDF directory: ")
    fileLoc = input()
    if(os.path.isfile(fileLoc)):
        break
    else:
        print("File cannot be found.")

print("Use an existing directory? Y/N")
direcState = input()

if(direcState == 'Y'):
    while True:
        print("Existing directory path: ")
        outputLoc = input()
        if(os.path.isdir(outputLoc)):
            break
        else:
            print("Directory cannot be found.")
elif(direcState == 'N'): 
    print("Directory path and name: ")
    outputLoc = input()
    os.mkdir(outputLoc)

print("Opening file...")
pdf = fitz.open(fileLoc)
for pageIndex in range(pdf.page_count):
    page = pdf.load_page(pageIndex)
    image = page.get_pixmap()
    image.save(f'{outputLoc}/img{pageIndex}.png', 'png')
    print(f'Saved img{pageIndex}')

print("Done.")

pdf.close()

    