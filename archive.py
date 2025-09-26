import zipfile
import base64

path = "задание/MyOs/MyVFS.zip"
file_zip = zipfile.ZipFile(path, 'r')
print(file_zip.filelist)



for file in file_zip.infolist():
    print(file.filename)

    


    if file.filename.lower().endswith(".txt"):
        with file_zip.open(file.filename, 'r') as file_text:
            print("------начинаю считывание файла: " + file.filename)
            for line in file_text:
                print(line)
    if file.filename.lower().endswith(".jpg"):
        with file_zip.open(file.filename) as file:
                    image_data = file.read()
                    base64_data = base64.b64encode(image_data).decode('utf-8') # <---------- разобраться в том, что происходит
                    print(f"Base64 (первые 100 символов): {base64_data[:100]}...")
file_zip.close()
