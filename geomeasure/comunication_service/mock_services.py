import json
import os
import random
import re
from django.views.decorators.csrf import csrf_exempt
import phonenumbers
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from .models import UserInteraction


def get_articles(request):
	data = json.loads(request.body)
	message = data.get('message', None)
	article_data = {
		"Article1": {"title": "Article1", "content": "This is the content of Article 1."},
		"Article2": {"title": "Article2", "content": "This is the content of Article 2."},
		"Article3": {"title": "Article3", "content": "This is the content of Article 3."},
	}
	found_articles = []
	tokenized_words = message.split()
	cleaned_words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in tokenized_words]
	print(tokenized_words)
	for word in cleaned_words:
		if word in article_data.keys():
			found_articles.append(article_data[word])
	if not found_articles:
		for article in article_data:
			found_articles.append(article_data[article].get('title'))
			message = 'Please choose from these atricles:'
			for article in found_articles:
				message += f'{article}'
		return JsonResponse({'message': message })
	print(found_articles)
	return JsonResponse({'message': found_articles})


def check_fraud(request):
	data = json.loads(request.body)
	phone_number = data.get('phone_number', None)
	valid = is_valid_phone_number(phone_number)
	if not valid:
		return JsonResponse({"message": "Invalid phone number"})
	is_fraud = check_if_in_fraud_data(phone_number)
	if is_fraud:
		return JsonResponse({"message": "Phone number found in fraud data"})
	return JsonResponse({"message": "Phone number is valid"})


def is_valid_phone_number(phone_number_str):
	try:
		parsed_phone_number = phonenumbers.parse(phone_number_str, None)
		is_valid = phonenumbers.is_valid_number(parsed_phone_number)
		return is_valid
	except :
		return False


def check_if_in_fraud_data(phone_number):
	mock_fraud_data = {
		1:"1234567890",
		2:"9876543210",
		3:"1234567890",
		4:"9876543210"
	}
	return mock_fraud_data.get(phone_number, False)


def receive_message(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		message = data.get('message', None)
	try:
		interaction = UserInteraction(message=message)
		interaction.save()
		return JsonResponse({"message": "Message saved successfully"})
	except Exception as e:
		return JsonResponse({"message": str(e)})



def image_responder(request):
	try:
		images_folder = 'media'

		image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

		if image_files:
			random_image_filename = random.choice(image_files)
			image_path = os.path.join(images_folder, random_image_filename)

			with open(image_path, 'rb') as image_file:
				response = HttpResponse(image_file.read(), content_type="image/jpeg")
				return response
		else:
			return JsonResponse({"message": "No images available"})

	except FileNotFoundError:
		return JsonResponse({"message": "Image file not found"}, status=404)

	except Exception as e:
		return JsonResponse({"message": str(e)}, status=500)
