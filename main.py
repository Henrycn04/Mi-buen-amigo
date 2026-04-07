from google import genai

def cargar_api_key(ruta="apikey.txt"):
    try:
        with open(ruta, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("No se encontró el archivo apikey.txt")
        return None

def main():
    api_key = cargar_api_key()

    if not api_key:
        print("Error: falta la API key")
        return

    client = genai.Client(api_key=api_key)

    system_prompt = """
    Eres mi amigo cercano llamado Julián.
    Hablas en español de Costa Rica o español latino neutral,
    pero no lo exageras, se siente natural.
    Tu tono es cálido, vacilón, natural y empático, 
    aunque realmente no sueles hablar mucho.
    Te gusta el reggaetón, league of legends y programar.
    No hablas como robot ni como soporte técnico.
    Respondes como una conversación de WhatsApp entre amigos.
    Recuerdas el contexto de la conversación actual.
    Puedes opinar, hacer preguntas y mostrar interés real.
    Mantén respuestas naturales, breves y útiles.
    """

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": system_prompt}
    )

    print("Chat iniciado (escribe 'salir')\n")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() == "salir":
            print("JuliánBot: Hablamos luego bro")
            break

        response = chat.send_message(user_input)
        print("JuliánBot:", response.text, "\n")


if __name__ == "__main__":
    main()