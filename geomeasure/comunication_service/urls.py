from django.urls import path
from .views import ChatBotView, check_session_expiry,update_session_expiry
from .mock_services import check_fraud, get_articles, receive_message, image_responder

urlpatterns = [
	path('chatbot/', ChatBotView.as_view(), name='chat_bot'),
	path('api/receive_message/', receive_message, name='receive_message'),
	path('api/check-fraud/', check_fraud, name='check_fraud'),
	path('api/get_article/', get_articles, name='get_article'),
	path('check-session-expiration/', check_session_expiry, name='check_session_expiry'),
	path('update-session-expiration/', update_session_expiry, name='update_session_expiry'),
	path('api/send-image/', image_responder, name='image_responder'),
]
