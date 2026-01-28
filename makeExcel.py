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


def cleanQuestions(q):
    questions = []
    blocks = q.strip().split('---')
    for block in blocks:
        print(block)


    return questions


def createExcel(q):
    pass


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


