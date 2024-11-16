from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/DialoGPT-small"  # Chatbot ligero para experimentos
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chatbot_response(user_input, chat_history_ids=None):
    # Tokenizar entrada del usuario
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Generar respuesta
    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    print("¡Bienvenido al chatbot! Escribe 'salir' para terminar.")
    chat_history_ids = None
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("¡Adiós!")
            break
        response = chatbot_response(user_input, chat_history_ids)
        print(f"Bot: {response}")
