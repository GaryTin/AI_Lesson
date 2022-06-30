import  urllib.request
import zipfile

def main():
    url="https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip"

    file_name = "horse-or-human.zip"
    dir = "Images/horse-or-human/validation/"
    urllib.request.urlretrieve(url,file_name)

    zip_ref = zipfile.ZipFile(file_name,"r")
    zip_ref.extractall(dir)
    zip_ref.close()


if __name__ == "__main__":
    main()