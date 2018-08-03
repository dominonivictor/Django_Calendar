from django import forms

#This object will be used to create a new Event giving a form to be filled by the user
class EntryForm(forms.Form):
    name = forms.CharField(max_length=100)#here we limit the event name to 100 chars
    date = forms.DateTimeField()#accepts only int and dashes (Y-M-D)
    description = forms.CharField(widget=forms.Textarea)#wider area for the
    #description of the event
