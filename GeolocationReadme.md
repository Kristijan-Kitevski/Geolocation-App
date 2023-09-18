Geolocation App with Integrated Chatbot
Overview
This Geolocation App is designed to provide measurement services and features, with an integrated chatbot for user interactions. The chatbot can respond to limited commands and validate phone numbers based on user input.

Features
- Geolocation services and features.
- User-friendly chat interface.
- Session management for tracking user interactions.
- Integration with external services, such as phone number validation.
- Article lookup based on user queries.
- Error handling for invalid commands.

Installation
To run the Geolocation App with an integrated chatbot on your local machine, follow these steps:

1. Clone this repository to your local system:

    `git clone git@github.com:Kristijan-Kitevski/Geolocation-App.git`

3. Navigate to the project directory:

4. Create a virtual environment (optional but recommended):

    `python -m venv venv`

6. Activate the virtual environment:

   On Windows:

    `venv\Scripts\activate`
   
   On macOS and Linux:

    `source venv/bin/activate`

8. Install the required Python packages:

    `pip install -r requirements.txt`

10. Apply database migrations:
  
   `python manage.py migrate`

11. Start the development server:

     `python manage.py runserver`

13. Access the application in your web browser.

Usage
1. Enter your message in the chat input field and press "Send" to send the message.
2. The chatbot will respond to commands and validate phone numbers based on your input.
3. Session management ensures your session remains active while interacting with the chatbot.

External Services
The application uses external services for phone number validation and geolocation data. Ensure that your Django settings are configured correctly to use these services.

Configuration
You can customize the chatbot's responses, session duration, and other settings in the Django project's settings file. Make sure to configure the database and other required settings for your deployment environment.

License
This Geolocation App with Integrated Chatbot is open-source software licensed under the MIT License.

Contributing
Contributions are welcome! Please follow the Contribution Guidelines when contributing to this project.

Authors
- Kristijan Kitevski
