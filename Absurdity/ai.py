import openai

# Set up the OpenAI API client
openai.api_key = "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"
completion = openai.Completion()

# Come up with something truly absurd
absd_prompt = 'Come up with something absurd in 5 words or less'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=absd_prompt,
  temperature=0,
  max_tokens=30,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

absurd_ai = response["choices"][0]["text"]

# Prompt the user for the artist and song idea
img_prompt = absurd_ai
print(absurd_ai)

response = openai.Image.create(
  prompt=img_prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)