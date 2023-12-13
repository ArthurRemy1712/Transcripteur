import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from openai import OpenAI
import os

# Configure ta clé API OpenAI
client = OpenAI(api_key='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')

def convert_and_transcribe():
    file_path = filedialog.askopenfilename()
           
            
            # Utiliser l'API OpenAI pour transcrire le fichier audio
    response = client.audio.transcriptions.create(
        file=open(file_path,"rb"),
        model="whisper-1",
        response_format='text'
     )
    text.insert(tk.END, response)

          
# Création de l'interface graphique
root = tk.Tk()
root.title("Transcription Audio par Arthur")


# Bouton pour choisir le fichier audio et lancer la transcription
button = tk.Button(root, text="Choisir un fichier audio ", command=convert_and_transcribe)
button.pack(pady=20)

# Zone de texte pour afficher la transcription
text = tk.Text(root, height=60, width=200)
text.pack(padx=20, pady=10, fill=tk.BOTH, side=tk.LEFT, expand=True)


root.mainloop()


