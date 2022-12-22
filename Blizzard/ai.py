import openai

# Set up the OpenAI API client
openai.api_key = "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"
completion = openai.Completion()

# Prompt the user for the artist and song idea
artist = input("Enter the name of the artist: ")
idea = input("Enter the idea for the song: ")

prompt = 'Write a ' + artist + ' rap song about ' + idea

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)
# Extract the completed song lyrics from the response
song_lyrics = response["choices"][0]["text"]

# Print the completed song lyrics
print(song_lyrics)
