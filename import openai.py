import warnings
import openai
warnings.filterwarnings("ignore", message=".*NotOpenSSLWarning.*")
# Read the OpenAI API key from the api.txt file
with open('api.txt', 'r') as file:
    openai.api_key = file.read().strip()

def get_ai_response(subject, question):
    # Combine the subject and question into a prompt
    prompt = f"Subject: {subject}\nQuestion: {question}\nAnswer:"
    
    # Make a request to OpenAI's API (ChatGPT)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change to another model if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,  # Limit the length of the response
        temperature=0.7  # Control the creativity of the response
    )

    # Get and return the generated response
    return response['choices'][0]['message']['content'].strip()  # Correct access to content

# Get subject and question from the user
subject = input("Enter the subject: ")
question = input("Enter the question: ")

# Call the function and display the result
result = get_ai_response(subject, question)
print(f"\nAI Response:\n{result}")
