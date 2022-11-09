"""

    https://www.youtube.com/watch?v=HaSPU6AdWeY&t=327s
    (for saveing data from form to database)

    if request.method == 'POST':
            x = request.POST['question']
            question_entry = Question(question_text= x,pub_date=ist)
            question_entry.save()
        return render(request,'home.html',date)

    
    output = Modelname.objects.filter(name__contains=value_user_serached)

     if request.method == 'POST':
        x = request.POST['inc']
        if x == 'submit':
            for y in result:
                no_of_likes = y.likes + 1
            resu = Blog.objects.update(likes=no_of_likes)
            content = {
            'masala':result,
            'length': no_of_likes,
            'like':resu
            }
            return render(request, 'read.html',content)

"""
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('main/',views.main,name='main'),
    path('new/',views.new,name='new'),
    path('but',views.but,name='but'),
    path('dis',views.dis,name='dis'),
    path('other',views.other,name='other'),
    path('test',views.test,name='test'),
    path('question',views.question,name='question'),
    #path('comment',views.comment,name='comment'),
    #path('enter_user',views.enter_user,name='enter_user'),
    path('sendmails_to_user',views.sendmails_to_user,name='sendmails_to_user'),
    path('categories/',views.categories,name='categories'),

  
]





















