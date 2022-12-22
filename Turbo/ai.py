from sportsipy.fb.team import Team
from sportsipy.fb.roster import Roster
import openai


def consortAI():
    # Set up the OpenAI API client
    openai.api_key = "YOUR_API_KEY"
    completion = openai.Completion()

    # Format the user input into a string for the OpenAI API
    prompt = f"{artist}: {idea}\n\n"

    # Request a completion from the OpenAI API
    response = completion.create(engine="davinci", prompt=prompt, max_tokens=1024)

    # Extract the completed song lyrics from the response
    prediction = response["choices"][0]["text"]

    # Print the completed song lyrics
    print(prediction)


def getTeamData(team_name):

    # determine team wins and losses
    # team_wins
    # team_losses

    # determine team strategy
    # team_strategy
    # team_tactics

    # determine team conditioning
    # team_mental_conditioning
    # team_physical_conditioning

    # determine team strength and skill
    # team_strength
    # team_skill