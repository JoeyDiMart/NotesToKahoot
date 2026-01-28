'''
Go to any AI and prompt it the following:

###
"Give me {N} questions to help me study for {E} in the following format:

Q: Question to be given?
A: Option A
B: Option B
C: Option C
D: Option D
CORRECT: {letter}
---
Q: Second Question to be given?
A: Option A
B: Option B
C: Option C
D: Option D
CORRECT: {letter}
---
etc.
---
Q: Last Question to be given?
A: Option A
B: Option B
C: Option C
D: Option D
CORRECT: {letter}
###

Be sure to paste the questions into AiGeneratedQuestions.txt ************************************
'''
import csv


def cleanQuestions(q):
    questions = []
    blocks = q.strip().split('---')
    for block in blocks:
        opts = block.strip().split("\n")
        ques = opts[0]
        a = opts[1]
        b = opts[2]
        c = opts[3]
        d = opts[4]
        correct = opts[5]
        correct_num = {'CORRECT: A': 1, 'CORRECT: B': 2, 'CORRECT: C': 3, 'CORRECT: D': 4}[correct]

        questions.append({
            'Question': ques,
            'Answer 1': a,
            'Answer 2': b,
            'Answer 3': c,
            'Answer 4': d,
            'Time limit': 30,
            'Correct answer': correct_num
        })

    return questions


def createExcel(questions, output_file='KahootQuestions.csv'):
    if not questions:
        print("❌ No questions found! Check your AiGeneratedQuestions.txt format.")
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Time limit', 'Correct answer']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for q in questions:
            writer.writerow(q)

    print(f"Done! check {output_file}\nMake sure you go to Kahoot and hit import from spreadsheet")

try:
    with open("AiGeneratedQuestions.txt", "r", encoding="utf-8") as f:
        questions_text = f.read()
    questions = cleanQuestions(questions_text)
    createExcel(questions)


except FileNotFoundError:
    print("❌ Error: AiGeneratedQuestions.txt not found!")
    print("Please create the file and paste your AI-generated questions into it.")
except Exception as e:
    print(f"❌ Error: {e}")


