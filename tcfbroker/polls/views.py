#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
#from django.views import generic
from django.template import loader


from .models import Choice, Question, Profile, Resource
import profile

# with template 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#without template 
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

def profile(request):
    all_profile = Profile.objects.order_by('-caiq_score') 
    template = loader.get_template('polls/profile.html')
    context = {
        'all_profile': all_profile,
    }
    #return HttpResponse("You're looking at profile view.")
    return HttpResponse(template.render(context, request))


def cspdetail(request, profile_id):
   
    select_profile = get_object_or_404(Profile, pk=profile_id)
    all_resources = Resource.objects.filter(cloud=profile_id)
    
    template = loader.get_template('polls/cspdetail.html')
   
    context = {
    'select_profile': select_profile,
    'all_resources': all_resources
    }
        
    return HttpResponse(template.render(context, request))
    

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) 
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#class ProfileView(generic.DetailView):
#   template_name = 'polls/profile.html'
#    context_object_name = 'cloud_profile'

   # def get_queryset(self):
    #    """Return the last five published questions."""
     #   return Question.objects.order_by('-pub_date')[:5]