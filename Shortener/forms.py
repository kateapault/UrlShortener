from django import forms


HOSTS = (
        ('Tinyurl', 'Tinyurl'),
        ('Isgd', 'Is.gd'),
		('Bitly', 'Bit.ly'),
        ('Google', 'Google URL Shortener'),
        ('Rebrandly', 'Rebrand.ly'),
        ('Madwire', 'm360.us'),
        )

class Urlform(forms.Form):
    url = forms.CharField(label="Url", max_length=200)
    host = forms.ChoiceField(choices=HOSTS)