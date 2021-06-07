from django.shortcuts import render, redirect
from .models import TodoList, Category


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["Title"]  # title
            content= request.POST["description"]
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            Todo = TodoList(title=title, content=content, due_date=date,
                            category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            # checked todos to be deleted
            checkedlist = request.POST["checkedbox"]
            todo = TodoList.objects.get(id=int(checkedlist))  
            todo.delete()  # deleting todo
    return render(request, "hello.html", {"todos": todos, "categories": categories})

