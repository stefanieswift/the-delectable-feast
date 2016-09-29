from django import forms


class ContactForm(forms.Form):
	recipe = forms.CharField(label="Your recipe")
	message = forms.CharField(label="Message")
	sender = forms.EmailField(label="Your email", required=False)
	name = forms.CharField(label="Your name")
