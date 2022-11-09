from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog, Mailing_list, Categories, Question  #, Comments
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator
import random


# <!--https://www.youtube.com/watch?v=HaSPU6AdWeY&t=327s (for saveing data
#        from form to database)-->
def home(request):
    res = Blog.objects.order_by('title')[:6]
    cat = Categories.objects.order_by('name')[:100000000]
    length = len(res)
    comments = Question.objects.order_by('posted_on')[:10]
    list_of_pics = [
        "/static/yot.png", "/static/youth.png", "/static/yoo.png",
        "/static/ONE.png"
    ]
    n = random.randint(0, 3)
    var = list_of_pics[n]
    content = {
        'masala': res,
        'len': length,
        'cat': cat,
        'var': var,
        'posts': comments,
    }
    return render(request, 'home.html', content)


def main(request):
    if request.method == 'POST':
        value = request.POST['searched']
        modified_value = value.capitalize()
        result = Blog.objects.filter(title__contains=modified_value)
        category = Categories.objects.order_by('name')[:10000000]
        length = len(result)
        content = {
            'masala': result,
            'length': length,
            'value': modified_value,
            'cat': category
        }
        return render(request, 'main.html', content)
    else:
        return render(request, 'main.html')


def sendmails_to_user(request):
    count = Mailing_list.objects.order_by('pk')[:100000]
    number = len(count)
    i = 1
    while i <= number:
        nam = Mailing_list.objects.get(pk=i).name
        mail = Mailing_list.objects.get(pk=i).email
        details = {'name': nam, 'mail': mail}
        html_tem = render_to_string("mail.html", details)
        txt_of_mail = strip_tags(html_tem)
        Email = EmailMultiAlternatives('! TEST EMAIL PLS EGNORE !',
                                       txt_of_mail, 'yakshitchhipa@gmail.com',
                                       [mail])
        Email.attach_alternative(html_tem, "text/html")
        Email.send()
        i = i + 1
    return HttpResponse("sab hua")


def new(request):
    which = request.GET.get('which')
    result = Blog.objects.filter(id=which)
    category = Categories.objects.order_by('name')[:10000000]
    for y in result:
        ch = y.categories
        na = y.title
    num = random.randint(0, 50)
    length = len(result)
    related = Blog.objects.filter(categories=ch).exclude(title=na)[:3]
    # send_mail("!! TEST MAIL !!","LOL, TSET EMAIL WORKED .",'yakshitchhipa@gmail.com',['chhipayakshit@gmail.com'],fail_silently=False)
    content = {
        'masala': result,
        'length': length,
        'cat': category,
        'num': num,
        'rel': related,
    }
    return render(request, 'read.html', content)


def but(request):
    if request.POST.get('action') == 'post':
        p_k = int(request.POST.get('postid'))
        a = Blog.objects.get(pk=p_k).likes
        pk_entry = Blog.objects.filter(pk=p_k).update(likes=a + 1)
    return JsonResponse({'result': a})


def dis(request):
    if request.POST.get('action') == 'post':
        d_k = int(request.POST.get('postid'))
        d = Blog.objects.get(pk=d_k).likes
        dk_entry = Blog.objects.filter(pk=d_k).update(likes=d - 1)
    return JsonResponse({'result': d})


def test(request):
    return render(request, 'blog.html')


def categories(request):
    which = request.GET.get('name')
    cat = Categories.objects.filter(id=which)[:20000000]
    category = Categories.objects.order_by('name')[:1000000]
    recent = Blog.objects.order_by('published_on').filter(categories=which)[:6]
    popular = Blog.objects.filter(categories=which).order_by('likes')[:6]
    alll = Blog.objects.filter(categories=which).order_by('views')[:10000000]
    num = random.randint(0, 50)
    list_of_col = [
        "-sky-500", "-sky-300", "-amber-400", "-red-500", "-amber-300",
        "-lime-200", "-lime-500", "-green-500", "-cyan-300", "-blue-600",
        "-indigo-600", "-violet-500", "-purple-400", "-fuchsia-500",
        "-pink-500", "-rose-600"
    ]
    lent = len(list_of_col)
    c = random.randint(0, 15)
    color = list_of_col[c]
    content = {
        'wh': cat,
        'masala_two': recent,
        'masala_thr': popular,
        'masala_fou': alll,
        'cat': category,
        'num': num,
        'col': color,
        'l': lent,
    }
    return render(request, 'model.html', content)


def other(request):
    category = Categories.objects.order_by('name')[:1000000]
    return render(request, 'other.html', {'cat': category})


def question(request):
    if request.method == 'POST':
        action_to_be_done = request.POST.getlist('action')
        if action_to_be_done == ['notify']:
            ques = request.POST['text']
            nam = request.POST['nam']
            Email_of_user = request.POST['email']
            new_question = Question(question=ques,
                                    Email_of_user_who_asked=Email_of_user,
                                    user=nam)
            new_question.save()
            return redirect("/#faq")
        if action_to_be_done == ['join']:
            name_of_user = request.POST['nam']
            Email_of_user = request.POST['email']
            new_entry_user = Mailing_list(name=name_of_user,
                                          email=Email_of_user)
            new_entry_user.save()
            return redirect("/#faq")
