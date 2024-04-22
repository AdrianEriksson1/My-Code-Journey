# HangMan

import random

words = [
    "mountain", "bicycle", "library", "sunflower", "watermelon",
    "giraffe", "crocodile", "pineapple", "television", "football",
    "baseball", "umbrella", "volcano", "rainbow", "cheetah",
    "elephant", "koala", "tiger", "guitar", "piano",
    "violin", "keyboard", "laptop", "octopus", "dolphin",
    "whale", "seahorse", "rocket", "spaceship", "helicopter",
    "airplane", "motorcycle", "snowboard", "skyscraper", "mosquito",
    "butterfly", "caterpillar", "dragonfly", "honeybee", "ladybug",
    "cucumber", "waterfall", "snowflake", "fireplace", "campfire",
    "backpack", "suitcase", "scissors", "hairbrush", "toothbrush",
    "toothpaste", "soccer", "basketball", "volleyball", "badminton",
    "tennis", "cricket", "pingpong", "tabletennis", "archery",
    "swimming", "surfing", "skating", "skiing", "snowboarding",
    "diving", "snorkeling", "hiking", "mountaineering", "rockclimbing",
    "rafting", "kayaking", "canoeing", "sailing", "fishing",
    "bungeejumping", "paragliding", "parachuting", "skydiving", "kitesurfing",
    "windsurfing", "painting", "drawing", "sculpture", "photography",
    "pottery", "origami", "knitting", "crocheting", "embroidery",
    "quilting", "calligraphy", "woodworking", "gardening", "cooking"
]
    





    
def guess():
    word = random.choice(words)
    word = "word"
    wrong_guesses = []
    hidden_word = "_" * len(word)
    print(hidden_word)
    while any(i for i in hidden_word if i == "_") and len(wrong_guesses) < len(word)+3:
        guess = input("\n\nEnter a letter to guess: ").lower()

        if len(guess) > 1:
            print("It can only be 1 letter\n")

        if guess in word:
            if word.count(guess) >= 2:
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_word = list(hidden_word)
                        hidden_word[i] = guess
            else:
                place = word.index(guess)
                hidden_word = list(hidden_word)
                hidden_word[place] = guess
            hidden_word = "".join(hidden_word)
            print(f"You guessed correctly! \n    {hidden_word} \nWrong guesses: {wrong_guesses}")

        
        else:
            wrong_guesses.append(guess)
            print(f"Sorry, no such letter in the word\n    {hidden_word} \nWrong guesses: {wrong_guesses}")
    else:
        if "_" in hidden_word:
            print("\nYou ran out of guesses")
        else:
            print("\nYou Guessed the Right Word! 🎉\n")
guess()




