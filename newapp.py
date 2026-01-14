from google import genai                               #gemini flash 2.5-new version

# Create a client and pass the API key here
client = genai.Client(api_key="type your api kry here")

print("AI Q&A Bot is running (type 'exit' to stop)")

while True:
    question = input("You: ").strip()

    if question == "":
        print("Please type a question.")
        continue

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Make the request to Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print("AI:", response.text)
