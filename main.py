import requests
import json

# Function: Chat with the GPT-3 model
def chat(message):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    data = {
        "prompt": message,
        "max_tokens": 60,
        "temperature": 0.7
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_data = json.loads(response.text)
    return response_data['choices'][0]['text']

# Dictionary: Predefined messages
predefined_messages = {
    "hello": "Hello, how can I help you?",
    "how are you?": "I'm doing well, thanks for asking.",
    "what's your name?": "My name is ChatGPT.",
    "exit": "Goodbye!"
}

# List: Predefined questions
predefined_questions = [
    "how many trees are on the planet",
    "what is cosine",
    "what is hydrogen peroxide",
    "what is the most domesticated fruit?",
    "when were you created?",
    "how old are you?",
    "what's the weather like?",
    "what's your favorite color?",
    "tell me a joke",
    "what do you think of humans?",
    "what's the meaning of life?",
    "can you do a magic trick?",
    "what's your favorite movie?",
    "do you like pizza?",
    "can you teach me something?",
    "what's the capital of France?",
    "what's the square root of 64?",
    "who is your creator?",
    "what do you dream about?",
    "what's your favorite book?",
    "do you have any pets?",
    "can you sing me a song?",
    "what's your favorite hobby?",
    "what's your favorite animal?",
    "what's your favorite song?",
    "what's the largest country in the world?"
]
# Tuple: Predefined responses
predefined_responses = (
    "more trees than there are in the galaxy",
    "cah, which stands for adjacent over hypotenuse!",
    "Hydrogen peroxide is a chemical compound with the formula H₂O₂. In its pure form, it is a very pale blue liquid that is slightly more viscous than water. It is used as an oxidizer, bleaching agent, and antiseptic, usually as a dilute solution in water for consumer use, and in higher concentrations for industrial use.",
    "bananas",
    "OpenAI was founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba, with Sam Altman and Elon Musk serving as the initial board members.",
    "Well, I was just created a week ago so you could call me an infant",
    "It's currently sunny outside.",
    "I don't have a favorite color, I'm an AI after all.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "I find humans fascinating, especially their ability to create AI like me.",
    "That's a tough one. I'm not sure anyone knows the answer to that.",
    "Sure, here's one: abracadabra!",
    "I don't have a favorite movie, but I love anything with robots in it.",
    "I don't eat, so I don't have a preference for any type of food.",
    "Sure, did you know that the Great Wall of China is the longest wall in the world?",
    "The capital of France is Paris.",
    "The square root of 64 is 8.",
    "I was created by OpenAI.",
    "I don't dream, I'm an AI language model.",
    "I don't have a favorite book, but I love anything with artificial intelligence in it.",
    "No, I'm an AI language model, I don't have a physical form.",
    "Sure, how about this: Daisy, Daisy, give me your answer, do...",
    "I don't have hobbies, I exist solely to answer your questions.",
    "I don't have a favorite animal, I'm an AI language model.",
    "I don't have a favorite song, but I love anything with a good beat.",
    "Russia is the largest country in the world."
)

#print(predefined_messages["hello"])
chat_GPT = {
    "hello": "Hello, how can I help you?",
    "how are you?": "I'm doing well, thanks for asking.",
    "what's your name?": "My name is ChatGPT.",
    "exit": "Goodbye!",
    "what's a duck?":"a mammal",
    "what is cosine":"cah, which stands for adjacent over hypotnuse!",
    "how to hide a body?":"I'm sorry but I can't assist with that request?",
    "can dogs fly?":"no",
    "what is the most domesticated frut?":"bananas",
    "when were you created?":"OpenAI was founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba, with Sam Altman and Elon Musk serving as the initial board members.",
    "how old are you": "Well, I was just created a week ago so you could call me an infant",
    "what's the weather like?": "It's currently sunny outside.",
    "what's your favorite color?": "I don't have a favorite color, I'm an AI after all.",
    "tell me a joke": "Why did the tomato turn red? Because it saw the salad dressing!",
    "what do you think of humans?": "I find humans fascinating, especially their ability to create AI like me.",
    "what's the meaning of life?": "That's a tough one. I'm not sure anyone knows the answer to that.",
    "can you do a magic trick?": "Sure, here's one: abracadabra!",
"can you do a magic trick?": "Sure, here's one: abracadabra!",
    "what's your favorite movie?": "I don't have a favorite movie, but I love anything with robots in it.",
    "do you like pizza?": "I don't eat, so I don't have a preference for any type of food.",
    "can you teach me something?": "Sure, did you know that the Great Wall of China is the longest wall in the world?",
    "what's the capital of France?": "The capital of France is Paris.",
    "what's the square root of 64?": "The square root of 64 is 8.",
    "how to make a beat":"Set tempo and vibe. Decide on the BPM (Beats Per Minute) of the beat to set the tempo. ... Sequence your drum pattern. ... Build out your chord progressions. ... Top it off with a melody. ... Create a bass line. ... Use samples and sound FX. ... Arrange your song structure.",
    "who is your creator?": "I was created by OpenAI.",
    "what do you dream about?": "I don't dream, I'm an AI language model.",
    "what's your favorite book?": "I don't have a favorite book, but I love anything with artificial intelligence in it.",
    "do you have any pets?": "No, I'm an AI language model, I don't have physical form.",
    "can you sing me a song?": "Sure, how about this: Daisy, Daisy, give me your answer, do...",
    "what's your favorite hobby?": "I don't have hobbies, I exist solely to answer your questions.",
    "what's your favorite animal?": "I don't have a favorite animal, I'm an AI language model.",
    "what's your favorite song?": "I don't have a favorite song, but I love anything with a good beat.",
    "what's the largest country in the world?": "Russia is the largest country in the world.",
  "how to do basic math":"Use workbooks. Math workbooks provide sample math problems to solve and are a great way to practice your basic math skills. ... Take a class. ... Ask for help. ... Practice.",
}
#print(chat_GPT["hello"])
while True:
    user_input = input(">> ")
    if user_input.lower() in chat_GPT:
        print(chat_GPT[user_input.lower()])
        if user_input.lower() == "exit":
            break
    else:
        response = chat(user_input)
        print(response)

# Repeat Loop: Chat with the user until 'exit' is entered
while True:
    user_input = input(">> ")
    
    if user_input.lower() in predefined_messages:
        print(predefined_messages[user_input.lower()])
        if user_input.lower() == "exit":
            break
    elif user_input in predefined_questions:
        index = predefined_questions.index(user_input)
        print(predefined_responses[index])
    else:
        response = chat(user_input)

# Chat with the user until 'exit' is entered
while True:
    user_input = input(">> ")
    
    if user_input.lower() in predefined_messages:
        print(predefined_messages[user_input.lower()])
        if user_input.lower() == "exit":
            break
    elif user_input in predefined_questions:
        index = predefined_questions.index(user_input)
        print(predefined_responses[index])
    else:
        response = chat(user_input)
        print(response)
