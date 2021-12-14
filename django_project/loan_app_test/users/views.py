from django.shortcuts import render, redirect  
from django.contrib import messages  
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm 
from users.forms import BankDetailsForm
from users.models import BankStatement
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import RequestContext


#1. Register
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in ')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def bankstatement(request):
    # Handle file upload
    if request.method == 'POST':
        form = BankDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = BankStatement(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST

            #return HttpResponseRedirect(reverse('users.views.bankstatement'))
            redirect('login')
    else:
        form = BankDetailsForm() # A empty, unbound form

    # Load documents for the list page
    documents = BankStatement.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'users/bank_statement.html',
        {'documents': documents, 'form': form}
    )

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated ')
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    
    context = {
        'u_form':u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

