from django.shortcuts import render

# Create your views here.
def home_screen_veiw(request):
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
    }

    return render(request, 'BlogApp/Home.html',context)
