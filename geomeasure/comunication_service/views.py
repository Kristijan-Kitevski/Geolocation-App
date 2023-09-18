from django.contrib.sessions.models import Session
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView


def update_session_expiry(request) -> None:
	session_key = request.COOKIES.get('chatbot_session')
	try:
		session = Session.objects.get(session_key=session_key)
		session.expire_date = timezone.now() + timezone.timedelta(minutes=10)
		session.save()
		return HttpResponse("Session updated successfully", status=200)
	except Session.DoesNotExist:
		return HttpResponse("Session not found", status=404)

def create_session(request):
	if not request.session.session_key:
		request.session.save()

def check_session_expiry(request):
	session_key = request.COOKIES.get('chatbot_session')
	if not session_key:
		create_session(request)
	try:
		session = Session.objects.get(session_key=session_key)
		last_activity_time = session.expire_date
		current_time = timezone.now()
		if last_activity_time is not None:
			time_difference = current_time - last_activity_time
			if time_difference.total_seconds() > 0:
				return JsonResponse({'message': 'Session ended'})
	except Session.DoesNotExist:
		return JsonResponse({'message': 'Session does not exist.'})
	return JsonResponse({'message': 'Session is active.'})


class ChatBotView(APIView):
	def get(self, request):
		create_session(request)
		return render(request, 'chat_bot.html')
