from Factivity.annual.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# index: show all work, most recent first
def index(request):
    logged_in = request.user.is_authenticated()
    categories = Category.objects.all();
    recent_activity = Activity.objects.all().order_by('-date')
    return render_to_response('annual/index.html', {'recent_activity': recent_activity,
                                                    'categories':categories,
                                                    'logged_in':logged_in})

def user(request, username):
    logged_in = request.user.is_authenticated()
    recent_activity = Activity.objects.all().filter(username=username)
    categories = Category.objects.all();
    owner = ( request.user.username == username )

    return render_to_response('annual/user_detail.html', {
                                                          'recent_activity' : recent_activity,
                                                          'username' : username,
                                                          'logged_in':logged_in,
                                                          'owner':owner,
                                                          'request':request,
                                                          'categories':categories})
    
def login_view(request):
    return render_to_response('annual/login.html')

def authenticate_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('Factivity.annual.views.index'))
        else:
            return HttpResponse('Uh oh, error.')
    else:
        return render_to_response('annual/login.html', {
                                                        'errors':True })
    return HttpResponse('Oh Yeah')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Factivity.annual.views.index'))

@login_required
def add(request):
    categoryid = request.POST['category']
    username = request.user.username
    description = request.POST['description']
    
    category = Category.objects.get(pk=categoryid)
    new_activity = Activity(username=username, description=description,
                            category=category)
    
    new_activity.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required
def delete(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    username = request.user.username
    if activity.username == username:
        activity.delete()
    
    return HttpResponseRedirect(reverse('Factivity.annual.views.user', args=[str(username)]))