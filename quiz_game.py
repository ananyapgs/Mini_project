questions=[
    {
        "prompt":"Which of the following is NOT one of the Seven Wonders of the Ancient World?",
        "options":["A. The Great Pyramid of Giza","B. The Hanging Gardens of Babylon","C. The Eiffel Tower","D. The Statue of Zeus at Olympia"],
        "answer":"C"
    },
    {
        "prompt":"Which wonder is the only one still standing today from the Seven Wonders of the Ancient World?",
        "options":["A. The Colossus of Rhodes","B. The Great Pyramid of Giza","C. The Lighthouse of Alexandria","D. The Mausoleum at Halicarnassus"],
        "answer":"B"
    },
    {
        "prompt":"Machu Picchu, one of the New Seven Wonders of the World, is located in which country?",
        "options":["A. Mexico","B. Peru","C. Brazil","D. Argentina"],
        "answer":"B"
    },
    {
        "prompt":"Which modern wonder is a giant statue of Jesus Christ located in Brazil?",
        "options":["A. The Moai Statues","B. Christ the Redeemer","C. The Colossus of Rhodes","D. The Terracotta Army"],
        "answer":"B"
    },
    {
        "prompt":"Petra, an ancient city carved into rock, is located in which country?",
        "options":["A. Egypt","B. Jordan","C. Greece","D. India"],
        "answer":"B"
    },
    {
        "prompt": "The Great Wall of China, one of the New Seven Wonders, was built to protect against invasions from which group?",
        "options": ["A. Romans", "B. Mongols", "C. Persians", "D. Greeks"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following is NOT one of the New Seven Wonders of the World?",
        "options": ["A. Taj Mahal", "B. Colosseum", "C. Chichen Itza", "D. Stonehenge"],
        "answer": "D"
    },
    {
        "prompt": "Which wonder, originally built as a tomb, is considered a symbol of love?",
        "options": ["A. Machu Picchu", "B. Taj Mahal", "C. Great Pyramid of Giza", "D. The Hanging Gardens of Babylon"],
        "answer": "B"
    },
    {
        "prompt": "Chichen Itza, a wonder located in Mexico, was built by which ancient civilization?",
        "options": ["A. Aztecs", "B. Incas", "C. Mayans", "D. Egyptians"],
        "answer": "C"
    },
    {
        "prompt": "Which of these ancient wonders was a massive bronze statue located on the island of Rhodes?",
        "options": ["A. The Statue of Zeus", "B. The Colossus of Rhodes", "C. The Lighthouse of Alexandria", "D. The Mausoleum at Halicarnassus"],
        "answer": "B"
    },
    {
        "prompt": "Where is the Christ the Redeemer statue located?",
        "options": ["A. Argentina", "B. Brazil", "C. Chile", "D. Peru"],
        "answer": "B"
    },
    {
        "prompt": "The ruins of the Lighthouse of Alexandria were located in which country?",
        "options": ["A. Greece", "B. Turkey", "C. Italy", "D. Egypt"],
        "answer": "D"
    },
    {
        "prompt": "Which wonder was a temple dedicated to the Greek goddess Artemis?",
        "options": ["A. Temple of Artemis at Ephesus", "B. Parthenon", "C. Colosseum", "D. Machu Picchu"],
        "answer": "A"
    },
    {
        "prompt": "Which of the following wonders is famous for its gladiator battles?",
        "options": ["A. Colosseum", "B. Petra", "C. Great Wall of China", "D. Machu Picchu"],
        "answer": "A"
    },
    {
        "prompt": "What material was primarily used in the construction of the Great Pyramid of Giza?",
        "options": ["A. Granite", "B. Limestone", "C. Marble", "D. Sandstone"],
        "answer": "B"
    }
]


def run_quiz(questions):
    score=0

    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        print("\n")
        answer=input("Enter your answer : (A, B, C or D) ").upper()
        if answer==question["answer"]:
            print("Correct,Hurray!!\n")
            score+=1
        else:
            print("Wrong\nThe correct answer is : "+question["answer"],"\n")
    print(f"\nYou got {score} out of {len(questions)} questions correct\n")

run_quiz(questions)