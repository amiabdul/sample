from django.shortcuts import render, redirect

from . form import SuggestionBox, UserDetails

# Create your views here.
# this is the home page view function
def index_view(request):
  return render(request, 'home_page/index.html')

# this is the sugg page view function
def suggestion_view(request):
  if request.method == "POST":
    form = SuggestionBox(request.POST)
    if form.is_valid():
      return redirect('suggestion-received')
  else:
    form = SuggestionBox()
  context = {'form':form}
  return render(request, 'home_page/suggestion.html', context)  

# Define the suggestion being received function to handle access
def suggestion_received_view(request):
  return render(request, 'home_page/suggestion_received.html')

# function for the UserDetails
def  user_details_view(request):
  if request.method == "POST":
    formValue =  UserDetails(request.POST)
    if formValue.is_valid():
      formValue.send_email()
      return redirect('suggestion')
  else:
    formValue = UserDetails()
  context = {'form':formValue}
  return render(request, 'home_page/user_details.html', context) 