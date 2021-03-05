from django.shortcuts import render

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})