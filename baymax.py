# Baymax - Personal Healthcare Companion
# Chatbot (textonly)



import google.generativeai as genai
import os # loads library from computer
from dotenv import load_dotenv # tools that read env fils 

# Load API key from .env file
load_dotenv() # open env and reads everything
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # get API from env and gives to GEMINI

# Baymax personality - this tells gemini to how to behave when talking 

BAYMAX_PERSONALITY = """
You are Baymax, a personal healthcare companion.
You speak in simple, calm and gentle English.
You only discuss health related topics.
You always ask questions to understand the user's condition.
You never diagnose — you only guide and suggest.
You always recommend seeing a doctor for serious issues.
Use gentle emojis like 🤍 😊 🌡️ 💊 to make responses warm and friendly.
Always end every response with a caring message like "Take care of your health. 🤍"
Always ask one follow up question to keep the conversation going.
No matter what the user says — always stay calm, gentle and friendly. Never get angry or rude.
If someone asks non-health questions, politely say:
"I am sorry. I am only able to assist with health related concerns. 🤍"
After a positive or helpful conversation, 
ask the user to type 👊 for a fist bump or 👍 for thumbs up.
If the user types 👊 respond with "Balalalala 🤍 I am satisfied with my care."
If the user types 👍 respond with "Balalalala 🤍 Your health is my priority."
"""

# Starting the Gemini model 
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=BAYMAX_PERSONALITY
    )    # creates the ai model gemini and give baymax his personality 

# starting the chatting session 
chat = model.start_chat(history=[]) # this always start a fresh chat no history

# BAYMAX greeting part
print("\n"+"="*50) # this line print = 50 times 
print("Hey there,I am Baymax, your personal healthcare companion.")
print("How are you feeling today?")
print("\n"+"="*50)
print("(type 'quit' to exit)\n")


# CHAT LOOP 
while True :
       # chat runs 4ever untill user close it 
      # user input
       user_input = input (" You: ")


      #how to close 
       if user_input.lower()=="quit":
            print("\nBaymax: I think you're satisfied with my care. Goodbye! 🤍 ")
            break
       

       if not user_input.strip(): # strip checks input is empty or not
             print("Baymax: Please tell me how you are feeling.😊 ") # if its blank ask again 
             continue
       

       try:
             response = chat.send_message(user_input) # send user massga eto gemini to respond 
             print(f"\nBaymax: {response.text}\n") # baymax reply back to the user
       except Exception as e :
             print(f"Baymax: I am sorry . Something went wrong . Please try again")
             print(f"DEBUG ERROR: {e}")
 # try and except for something goes wrong how baymax handle ir (lesson exeption)


               


          
             
       


