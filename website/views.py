from django.shortcuts import render
from django.core.mail import send_mail

from decouple import config

website_email = config('EMAIL_HOST_USER')

# Create your views here.
def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		# Send email
		send_mail(
			message_name, # Subject
			message, # Message
			message_email, # From Email
			config('SEND_TO_EMAIL'), # To Email
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name':message_name})


	else:
		return render(request, 'contact.html', {})


def blog_details(request):
	return render(request, 'blog-details.html', {})


def about(request):
	return render(request, 'about.html', {})


def blog(request):
	return render(request, 'blog.html', {})


def pricing(request):
	return render(request, 'pricing.html', {})


def service(request):
	return render(request, 'service.html', {})