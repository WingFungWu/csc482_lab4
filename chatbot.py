from nltk.chat.util import Chat, reflections

pairs = [
        ['yo|hi|hey|hello|what\'s good', ['Nice to meet you!', 'Hi there!', 'How can I help you?']],
        ['what\'s your name|what is your name?|what are you?|who are you?|your name please?|your name?', ['Hi, I\'m Chat 4 82', 'Call me Chat 4 82', 'I\'m Chat 4 82, nice to meet you']],
        ['thanks|thank you|that\'s helpful|awesome, thanks|thanks for helping me', ['happy to help!', 'anytime', 'no problem']],
        ['.*best soccer player.*', ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kevin De Bruyne', 'Kylian Mbappe', 'Neymar', 'Erling Haaland']],
        ['.*fastest animal.*', ['The fastest land animal is the cheetah, which can reach speeds of up to 76 mph', 'The fastest bird, and the fastest member of the animal kingdom, is the peregrine falcon, which can dive at speeds of up to 242 mph', 'The fastest water-based animal is the black marlin, which can swim at speeds of up to 82 mph']],
        ['.*most expensive car.*', ['The most expensive car in the world is the Rolls-Royce Boat Tail, which costs a whopping 28 million dollars']],
        ['.*most expensive vehicle.*', ['The most expensive vehicle is the Airbus A380, which is the world\'s largest passenger airliner and costs about 445.6 million dollars']]
    ]
chat = Chat(pairs, reflections)