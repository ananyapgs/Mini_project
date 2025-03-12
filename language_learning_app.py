import random


words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "lo siento", "english": "sorry"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "buenos días", "english": "good morning"},
    {"spanish": "buenas noches", "english": "good night"},
    {"spanish": "cómo estás", "english": "how are you"},
    {"spanish": "bien", "english": ["well","good"]},
    {"spanish": "mal", "english": "bad"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "tiempo", "english": "time"},
]

def quiz_user(words):
    random.shuffle(words)
    score=0
    for word in words:
        print(f"What is the English translation of the word '{word['spanish']}' ?")
        user_answer=input("Your answer :").strip().lower()
        correct_answer=[ans.lower() for ans in word["english"]]
        if user_answer in correct_answer:
            print("Correct Answer!!\n")
            score+=1
        else:
            print(f"Your answer is wrong.\nThe correct answer is '{word['english']}'.\n")
    print(f"\nQuiz Completed!!!!\nYour Score : {score}/{len(words)}")

def main():
    print("Welcome to Language Learning App")
    input("Press Enter to start the quiz....")
    quiz_user(words)

if __name__=='__main__':
    main()
