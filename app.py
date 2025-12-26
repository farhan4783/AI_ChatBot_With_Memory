from database import init_db
from memory import save_message, get_recent_memory
from llm import generate_response

def build_prompt(user_id, user_input):
    memory = get_recent_memory(user_id)

    prompt = "You are a helpful AI chatbot.\n\n"

    if memory:
        prompt += "Conversation so far:\n"
        for role, content in memory:
            prompt += f"{role.capitalize()}: {content}\n"

    prompt += f"\nUser: {user_input}\nAssistant:"
    return prompt

def chatbot():
    init_db()
    user_id = "user_001"   # later replace with login/JWT
    print("🤖 AI Chatbot with Memory (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        save_message(user_id, "user", user_input)

        prompt = build_prompt(user_id, user_input)
        response = generate_response(prompt)

        print("Bot:", response)

        save_message(user_id, "assistant", response)

if __name__ == "__main__":
    chatbot()
