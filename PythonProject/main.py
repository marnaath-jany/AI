import json
from difflib import get_close_matches

def load_kmowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_kmowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.60)
    return matches[0] if matches else None

def get_answer_for_question(question: str, kwonledge) -> str | None:
    for q in kwonledge["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chat_bot():
    knowledge: dict = load_kmowledge("Knowledge.json")

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["answer"] for q in knowledge["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge)
            print(f'Bot: {answer}')
        else:
            print('Bot: Sorry, I didn\'t find that answer. can you teach me.')
            new_answer: str = input('Type your answer or "quit" to quit: ')

            if new_answer.lower() != 'quit':
                knowledge["questions"].append({"question": user_input, "answer": new_answer})
                save_kmowledge("Knowledge.json", knowledge)
                print("Bot: Thank you!")


if __name__ == '__main__':
    chat_bot()