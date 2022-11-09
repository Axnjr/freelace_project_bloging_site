"""
<1st section>

#VIEWS/APP                                               #URL/APP                                  #OUTPUT
def secret(request):                             time1 = ist.strftime("%H:%M")                 When url is 
    return HttpResponse("this is secret page")   urlpatterns = [                               127.0.1:8000/time1
                                                    path(time1,views.secret,name='secret'), ]  then 'this is secret
                                                                                                page' will be shown.
#time1 = current time ex: 19:22 

<2nd section>

#VIEWS/APP                                                   #URL/APP                                       #OUTPUT
def detail(request, question_id):      path('<int:question_id>/detail/', views.detail, name='detail'),   when url is 
    context = {                                                                                          /3(any number)/detail
        'question_id':question_id,                                                                       then output.
        'heading': 'DETAILS'
    }
    return render(request ,'trytwo.html',context)

<3rd section>

#VIEWS/APP 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:20]    # this is way to access models
    latest_choice_list = Choice.objects.order_by('-choice_text')[:20]     # [:20] is how many data entries should be shown
    #output = ' , '.join([q.question_text for q in latest_question_list]) # is joing ',' with data entries   
    #return HttpResponse(output)
    content = {
        'latest_question_list': latest_question_list,
        'latest_choice_list': latest_choice_list,
    }
    return render(request , 'try.html',content)
    
"""



## Storage section

"""
 
    {% if searched %}
        <br><br>
        <h1 class="text-black py-6 text-5xl font-semibold">I found these topics ...</h1>
        <ul class="list-inside">
      kahi bhi paste kar diya <li class="list-inside list-decimal text-2xl font-semibold"><a href="#">{{blog.title}}</a></li>
        </ul>
    {% endif %}
        <p class="text-black pb-4 font-semibold border-b-8 border-black w-3/4 text-center"> </p>
        <p class="para font-semibold">{{blog.blog_one}}</p>
        <br><br><br>
 <form method="get">
                        {% csrf_token %}
                        <button class="like" name="liked" onclick="do_like()">like</button>
                    </form>
        <p class="para font-semibold">{{blog.blog_two}}</p>
        <br><br><br>
        <p class="para font-semibold">{{blog.blog_three}}</p>
        <br><br><br>
        <p class="para font-semibold">{{blog.blog_four}}</p>
        <br><br><br>
        <p class="para font-semibold">{{blog.blog_five}}</p>-->
   
    <!--<h1 class="text-4xl text-black" ><a href="/blogs">Post blogs</a></h1>-->"""