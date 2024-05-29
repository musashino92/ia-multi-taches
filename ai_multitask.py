
import openai
import subprocess
import os

# Configurez votre clé API OpenAI
openai.api_key = 'YOUR_API_KEY'

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def interpret_command(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write("")
        return f"Fichier '{file_path}' créé avec succès."
    except Exception as e:
        return str(e)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)

def delete_file(file_path):
    try:
        os.remove(file_path)
        return f"Fichier '{file_path}' supprimé avec succès."
    except Exception as e:
        return str(e)

def process_natural_language_command(natural_language_command):
    if "créer un fichier" in natural_language_command:
        file_path = natural_language_command.split("nommé ")[1].strip().replace("'", "")
        return create_file(file_path)
    elif "lire un fichier" in natural_language_command:
        file_path = natural_language_command.split("nommé ")[1].strip().replace("'", "")
        return read_file(file_path)
    elif "supprimer un fichier" in natural_language_command:
        file_path = natural_language_command.split("nommé ")[1].strip().replace("'", "")
        return delete_file(file_path)
    else:
        action = interpret_command(natural_language_command)
        return execute_command(action)

def main():
    print("Bienvenue dans l'IA multi-tâches!")
    while True:
        command = input("Entrez une commande : ")
        if command.lower() in ["quitter", "exit"]:
            break
        result = process_natural_language_command(command)
        print(result)

if __name__ == "__main__":
    main()
