from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyDh57VQ1HK1fhFg8MS0jP8sGYyxX2DNyIM")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="que dia é hoje?"
)
print(response.text)


