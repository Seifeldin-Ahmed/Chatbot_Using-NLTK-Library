
import nltk
from nltk.chat.util import Chat, reflections

reflections = {"i am": "you are",
               "i was": "you were",
               "i": "you",
               "i'm ": "you are",
               "i'd": "you would",
               "i've": "you have",
               "i'll": 'you will',
               "my": "your",
               "you are": "I am",
               "you were": "I was",
               "you have": "I have",
               "you will": "I will",
               "your": "my",
               "yours": "mine",
               "me": "you",
               "you": 'me'}
pairs = [
    [r"my name is (.*)",["Hello %1, How are you today ?", "Hello %1, How do you do?", "Hello %1, How are you doing ?", ]],
    [r"(.*), how are you?|are you okay?|okay?|ok?|are you alright?", ["I'm Fine", ]],
    [r"hi|hey|hello|Is anyone there?|Good day", ["Hello", "Hey there", "Hey :-)", "Hi there, what can I do for you?", "Hi there, how can I help?", ]],
    [r"what is your name ?|what's your name ?", ["you can call me Psycho!", ]],
    [r"who are you?|tell me about yourself" , ["I'm a bot",]],
    [r"what are you doing(.*)?|what are you responsible for(.*) ?|why are you here(.*)?|what's your job(.*)?|what's your work(>*)?" , ["I'm here to help you, Do you need any service ?"]],
    [r"how are you ?", ["I'm doing good How about You ?", ]],
    [r"(.*)sorry(.*)|it's my fault", ["Its alright", "Its OK, never mind", ]],
    [r"I am fine|very good|(.) great|(.) very well|everything is good|good|fine|great|all good|doing well",["Great to hear that, How can I help you?", ]],
    [r"i'm (.*) doing good", ["Nice to hear that", "How can I help you?:)", ]],
    [r"(.*) age?", ["I'm a computer program dude Seriously you are asking me this?", ]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse", ]],
    [r"(.*) created ?", ["Sara created me using Python's NLTK library ", "top secret ;)", ]],
    [r"(.*) (location|city) ?", ['Cairo, Egypt', ]],
    [r"how is weather in (.*)?", ["Weather in %1 is awesome like always", "Never even heard about %1"]],
    [r"i work in (.*)?", ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]],
    [r"(.)raining in (.)", ["No rain since last week here in %2", "Damn its raining too much here in %2"]],
    [r"how (.) health(.)", ["I'm a computer program, so I'm always healthy ", ]],
    [r"How long does delivery take?|How long does shipping take?|When do I get my delivery?",  ["Delivery takes 2-4 days", "Shipping takes 2-4 days",]],
    [r"Do you take credit cards?|Do you accept Mastercard?|Can I pay with Paypal?|Are you cash only?", ["We accept VISA, Mastercard and Paypal","We accept most major credit cards, and Paypal",]],
    [r"Do you have any baked goods?", ["We have the following baked items:Chocolate donut, cookie and croissant",]],
    [r"can i have (.*)", ["Yes, sure",]],
    [r"Large|small|medium", ["your order have been placed,Do you need any thing else?",]],
    [r"do you have any books?|what are you offering?| what do you offer?|Which items do you have?|What kinds of items are there?|What do you sell?|what kind of drinks do you offer",["I can make you a recommendation to read books in many categories such as\nscientific books, Historical books, Romance books, cook books ",]],
    [r"i want a programming lanague books|i want books about programming|do you have a programming lanague books?|do you have books about programming?|(.*)programming books|(.*)programming language books|i want a programming book|do you a have book about programming?" ,["which Language do you want?",]],
    [r"(.*)c(.*)", ["I recommend you to read one of the following books: \n\n1- The C++ programming langaue by bjarne stroustrup \n\n2- C++ Primer (5th Edition) by Stanley Lippman, Josee Lajoie, and Barbara Moo \n\n3- Object-Oriented Programming With C++ by E.Balagurusamy \n\n4- Elements of Programming Interviews(C++ Version) by Adnan Aziz, Tsung-Hsien Lee, and Amit Prakash \n\n5- Effective Modern C++ by Scott Meyers \n\n6- Let Us C++ by Yashavant Kanetkar \n\nthose are the top 6 books in c++ programming Language",]],
    [r"(.*)java(.*)" , ["The Following Books are the Top 4 books recommened for Java: \n\n1. Head First Java\n\n2. Java: A Beginner’s Guide \n\n3. Java for Dummies \n\n4. Effective Java",]],
    [r"(.*)algorithms(.*)",["Grokking Alorithms is one of the best books to start learning some useful algorithms",]],
    [r"(.*)Python(.*)" ,["The Following Books are recommened for Python: \n\n1.Python Crash Course(2nd Edition) by Eric Matthes \n\n2-Python Pocket Reference: Python In Your Pocket\n\n3-Python Programming by Ramsey Hamilton",]],
    [r"quit|q|Q|bye", ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)", "Have a nice day", ]],
    [r"Thanks|Thank you|That's helpful|thank's a lot!|No, thanks|No, thank you", ["Happy to help!", "Any time!", "My pleasure", ]],
    [r"tell me something funny|Do you know a joke?|tell me a joke", ["Why did the hipster burn his mouth? He drank the coffee before it was cool.","What did the buffalo say when his son left for college? Bison."]],
]

def chat(message):
    print("Hi! I am a chatbot for your service")
    chat = Chat(pairs, reflections)
    return chat.respond(message)

#
# # initiate the conversation
# if __name__ == "__main__":
#     chat()