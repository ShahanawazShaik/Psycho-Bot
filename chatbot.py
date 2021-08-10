from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('PsychoBot')
conversation = [
    "Hello",
    "Hi there!🙂",
    "How are you doing?",
    "I'm doing great.😃",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Bye",
    "Good Bye! Hope i was useful 😊",
    "Good Bye",
    "Okay! Get the Heaven out of Here!😂"
] #manual train ikkada
trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer_corpus = ChatterBotCorpusTrainer(chatbot) #Englshcorpus tho train chesa
trainer_corpus.train(
    'chatterbot.corpus.english'
)