from django import forms

# class for the suggestion box
class SuggestionBox(forms.Form):
  suggestion = forms.CharField(widget=forms.Textarea)


# class for the user details
class UserDetails(forms.Form):
  firstName = forms.CharField(max_length=100)
  LastName = forms.CharField(max_length=100)
  email = forms.EmailField()
  
  def send_email(self):
    print(f"Sending email from {self.cleaned_data['email']}")