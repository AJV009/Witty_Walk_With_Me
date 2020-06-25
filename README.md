# Witty Walk With Me
Project submitted for Facebook AI Hackathon on Devpost.
- [FB AI Hackathon link](https://fbai2.devpost.com/)
- [Devpost project link](https://devpost.com/software/witty-walk-with-me)

## Inspiration
I got the inspiration to develop a smart walking start from my relatives and my father gave me the idea and mum helped in building the walking stick. This was really fun. And my first Devpost & FB Hackathon. 
**A Walking stick built for the people who are alone.**

A quick overview regarding people living alone.
**Ex.** If, when people around you hear you saying "Hey my heart is paining badly!" they will surely rush you to the nearest hospital or at-least call your nearest/closest friend/neighbor/relative, and done you are almost saved!
But now think what if you were alone in this situation, and what if that was a **sign of a Heart Attack**. You are probably dead by the time someone realizes that there is no movement from this house for a long time!
And this is where my "Witty" comes to scene! Witty intelligently understands the users distress calls and triggers a event like sms or call as per configuration.

Some document on the intenet supporting this case
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6199841/

**Problems faced by the “elderly staying alone”**
- ![Survey Image](/1img.jpg)

## What it does (current stage)
- Listens to users distress sounds.
- Creates alarms based on different distress voices. (sends msgs)

## How we built it
- Wit.ai (FB NLP API). It was very satisfying to see a actual NLP service working in my project. I trained the Wit.ai with many negative help regarding statements.
- Twilio for alerts (sms alerts). Applied a simple if-else logic to trigger events.

We triggered a sms event from twilio when a negative statement was detected from Wit.ai trained model! 😍

## Challenges we ran into
I faced a ton of challenges in this project.
- Everything from starting to end was a challenge cause it was new. Like finding wake word detection library but then Jetson Nano wouldn't support some of them.
- Firstly due to lock-down I couldn't get cheaper and lightweight hardware which could be used for the project purpose, so had to stick with a huge "Jetson Nano" which I got in a old idea submission contest and hardware accessories in India is very costly, that development is always hindered in some way!
- Microphone battery died half way had to wait a lot but then found the a good old camera's microphone working good.
- Am really new to developing a whole project involving API's so it took some time to figure out code and making it safer!
- I messed around with the project logic a million times, I had to go on changing the way the idea had to be implemented.
- Everyday the main code would change!

## Accomplishments that we're proud of
- My very first hackathon project
- Feel in love with Wit.ai (now am gonna use it as a bot service for new projects)
- Got to explore more using Python
- Tried Twilio (I had seen people sending sms from devices but didn't know that this was easy)
- I feel confident now to participate in other public hackathons.

## What I learned
- Python intermediate
- Using API services in Python
- Using Twilio
- Wit.ai

## What's next for Witty Walk With Me
- PyTorch CV for surrounding environment detection.
- Fold-able wheels attached under the stand so that it can move around the house also pull the user to a specific path just like a autonomous car.
- Ultrasonic based object detection so that it can work without light too.
- Use lighter board such as RPI Nano and more sensitive microphone, make the whole project smaller and safe for kids too.
- Audio device pair-able for voice based interaction.
- **I have a very good feeling that bots like "Witty" will be needed a lot in houses where people live alone with no one to assist.**


### Some understandable demo code
```python
import json
json_file = open('keys.json')
json_data = json.load(json_file)
keys = json_data["api_keys"]

access_token = keys[:][0]['wit']
account_sid = keys[:][0]['tsid']
auth_token  = keys[:][0]['tauth']

from wit import Wit
client = Wit(access_token)
resp = None
with open('temp.wav', 'rb') as f:
  resp = client.speech(f, {'Content-Type': 'audio/wav'})

text = resp['text']
trait_confidence = resp['traits']['help'][0]['confidence']
trait_value = resp['traits']['help'][0]['value']

from twilio.rest import Client
T_MSG = "Hi, you have a emergency msg from your dear! -> '"+text+"!'"
client = Client(account_sid, auth_token)

if trait_value=='call' and trait_confidence>=0.75:
    message = client.messages.create( to="+91xxxxxxxxxx", from_="+1xxxxxxxxxx", body=T_MSG)
```
