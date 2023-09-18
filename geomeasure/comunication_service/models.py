from django.db import models

class UserInteraction(models.Model):
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	# this model should have a foreign key to the user model and a foreign key to the session model
	
	def __str__(self):
		return f"{self.user_id} - {self.timestamp}"