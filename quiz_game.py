questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
     },
     {
        "prompt": "Which of the following is a fruit?",
        "options": ["A. Spinach", "B. Tomato", "C. Celery", "D. Broccoli"],
        "answer": "B"
     },
     {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
     },
     {
        "prompt": "Who wrote 'The Hunger Games' book?",
        "options": ["A. Suzanne Collins", "B. Mark Twain", "C. Stephen King", "D. Danielle Steel"],
        "answer": "A"
     },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper()   
        if answer == question["answer"]:
            print("Correct! \n")
            score += 1
        else:
            print("Incorrect, the correct answer was", question["answer"], "\n")  
    print(f"You got {score} out of {len(questions)} questions correct.")      
           
run_quiz(questions)            
