import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.
def home_screen_veiw(request):
    if request.user.is_authenticated:

        list = []
        list.append("Ist Item")
        list.append("2nd Item")
        list.append("3rd Item")
        list.append("4th Item")
        list.append("5th Item")
        list.append("6th Item")
        list.append("7th Item")

        context = {
            "Content1": "This is First Conent",
            "Content2": "This is Second Content",
            "ListSummary": ("List has item "+ str(len(list)) + "As Below : "),
            "ListItem": list,
            "Name": request.user
        }
        return render(request, 'BlogApp/Home.html',context)
    else:
        return redirect('login')

def vw_Upload(request):
    if request.method =="POST":
        file = request.FILES["fileToUpload"]
        fs = FileSystemStorage()
        fs.save(file.name,file)
        return redirect('/files')
    if request.method=="GET":
        return render(request, 'BlogApp/Upload.html')

def vw_Files(request):
    fs = FileSystemStorage()
    # os.listdir(path)
    print(fs.path)
    print(settings.MEDIA_ROOT)
    lst=list()
    for file in os.listdir(settings.MEDIA_ROOT):
        lst.append(
            {
                "FileName": file,
                "FileUrl":fs.url(file) 
            }
        )
    return render(request, 'BlogApp/Files.html', context={"ItemCount": len(lst), "Files": lst })