# OpenAI-Text-Compliation

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>

2. Install dependencies:
   
   pip install -r requirements.txt

4. You’ll need an API key from OpenAI to use GPT models. Sign up and create an API key

     place key here :
      
       api_key = "your_openai_api_key_here"

6. Run the application:

   
        uvicorn main:app --reload

     Open your web browser.

     Enter the following URL in the address bar:

       http://127.0.0.1:8000/docs

     Locate the /complete-text Endpoint:

   In the Swagger UI, find the /complete-text endpoint listed under the POST method.

   Click the "Try it out" Button:

   There will be a "Try it out" button. Click it to enable input for the request body.
   
   Enter the Request Body:

   In the request body text area :
   
         {
           "prompt": "Once upon a time"
        }

   
   Click the "Execute" Button:

