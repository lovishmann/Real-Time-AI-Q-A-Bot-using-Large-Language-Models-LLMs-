import google.generativeai as genai
                                                                               #older version-gemini 1.5 flash.
# Paste your Gemini API key below
genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

print("AI Q&A Bot is running (type 'exit' to stop)")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(question)
    print("AI:", response.text)
