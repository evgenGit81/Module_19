from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse
from .forms import UserRegister
class Platform(TemplateView):

    title = 'Магазинчик'
    main_head = "Добро пожаловать в магазин по покупке игр!"

    extra_context = {
        'main_head': main_head,
        'title': title,
        }
    template_name = 'index.html'


def catalog(request):
    main_head = "Вы в каталоге. Выбирайте что хотите!"
    game_title = Game.objects.values("title", "cost", "description")
    len_cat = len(game_title)
    context = {
            'game_title': game_title,
            'len_cat': len_cat,
            'main_head': main_head,

            }
    return render(request, 'catalog.html', context)


def bag(request):
    title = "корзина"
    main_head = "Корзина."
    text = "К сожалению ваша сумочка слишком мала, чтобы унести в ней такое изделие! :( Возьмите, пожалуйста, сумку побольше."
    context = {
        "title": title,
        "main_head": main_head,
        "text": text,
    }
    return render(request, 'bag.html', context)

def fmenu(request):
    return render(request, 'menu.html')


def sign_up_by_django(request):
    title = "Регистрация"
    users = Buyer.objects.values_list("name")
    main_head = "Регистрация"
    form = UserRegister()
    context = {
        'form': form,
        'main_head': main_head,
        'title': title,
    }

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.username = form.cleaned_data['username']
            form.password = form.cleaned_data['password']
            form.repeat_password = form.cleaned_data['repeat_password']
            form.age = form.cleaned_data['age']
            for i in range(len(users)):
                if form.username in users[i][0]:
                    return HttpResponse("Пользователь с таким именем уже существует")
            if form.password != form.repeat_password:
                return HttpResponse("Пароли не совпадают!")

            Buyer.objects.create(name=form.username, balance=0, age=form.age)

            return HttpResponse(f"Приветствуем, {form.username}!")


    return render(request, "registration_page.html", context=context)


def post_gm(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts,
    }
    return render(request, context=context)