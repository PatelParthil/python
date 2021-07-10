from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    name="PyBot",
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.BestMatch"]
)

small_talk = [
      'hiiii',
      'hi',
      'how are you?',
      'I m cool.',
      'fine, you?',
      'always cool.',
      'I am ok',
      'glad to hear that.',
      'I feel  awesome',
      'excellent , glad to hear that.',
      'not so good',
      'sorry to hear that.',
      'what is your name?',
      'I am pybot.',
      'Byee',
      'Good byeee, Have a nice day!!!'
]

math_talk = [
      'talk about anything else?',
      "Let's talk about Math.I know some mathametics theorems.",
      'pythagorean theorem',
      'a squared plus b squared equals c squared.'
      'law of cosines',
      'c**2 = a**2 + b**2 -2 * a * b * cos(gamma)'
]

gen_talk = [
        'which language you understand?',
        'I love english and i understand it very well.',
        'name of prime minister of india.',
        'Narendra Modi',
        "tell me today's weather.",
        'Clear with temperature : 34.00 C',
        "let's talk about cricket",
        'Well, in india ipl is famous cricket league',
        'is there any ipl match today?',
        'Yes, Rajasthan Royal VS Panjab Kings'
    ]

list_trainer = ListTrainer(bot)

for item in (small_talk, math_talk,gen_talk):
    list_trainer.train(item)


corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

while True:
    try:
        bot_input = input("You: ")
        bot_response = bot.get_response(bot_input)
        print(f"{bot.name}: {bot_response}")
        if bot_input=="byee" or bot_input=="Byee":
            break
    except(keyboardInterrupt, EOFError, SystemExit):
        break;
