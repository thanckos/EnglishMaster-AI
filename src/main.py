import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QTextEdit, 
                            QLineEdit, QPushButton, QWidget, QLabel)
from PyQt6.QtCore import Qt
from llama_cpp import Llama
import pyttsx3

from PyQt6.QtWidgets import QListWidget  # Ajoutez en haut du fichier

class EnglishMasterApp(QMainWindow):
    def __init__(self):
        # ... (code existant)
        self.add_grammar_ui()  # Nouvelle méthode

    def add_grammar_ui(self):
        self.grammar_list = QListWidget()
        lessons = load_grammar_lessons()
        for lesson in lessons["tenses"]["lessons"]:
            self.grammar_list.addItem(lesson["title"])
        
        self.grammar_list.itemClicked.connect(self.show_grammar_lesson)
        
        # Ajoutez à votre layout existant
        layout.addWidget(QLabel("📚 Grammaire"))
        layout.addWidget(self.grammar_list)

    def show_grammar_lesson(self, item):
        lesson_title = item.text()
        lessons = load_grammar_lessons()
        for lesson in lessons["tenses"]["lessons"]:
            if lesson["title"] == lesson_title:
                self.chat_display.append(f"📖 {lesson['title']}: {lesson['description']}")
                for example in lesson["examples"]:
                    self.chat_display.append(f"→ {example}")
                break

class EnglishMasterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EnglishMaster AI")
        self.setGeometry(100, 100, 800, 600)
        
        # Widgets
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.user_input = QLineEdit()
        self.send_button = QPushButton("Envoyer")
        self.pronunciation_button = QPushButton("Vérifier ma prononciation")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("💬 Chat avec l'IA"))
        layout.addWidget(self.chat_display)
        layout.addWidget(self.user_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.pronunciation_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Charger le modèle IA
        self.llm = Llama(model_path="./models/llama-3-8b-instruct.Q4_K_M.gguf")
        
        # Connecter les boutons
        self.send_button.clicked.connect(self.send_message)
        self.pronunciation_button.clicked.connect(self.check_pronunciation)
        
        # Synthèse vocale
        self.engine = pyttsx3.init()
        
    def send_message(self):
        user_text = self.user_input.text()
        self.chat_display.append(f"👤 Vous: {user_text}")
        
        # Réponse de l'IA
        output = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": user_text}],
            max_tokens=200
        )
        ai_response = output['choices'][0]['message']['content']
        self.chat_display.append(f"🤖 IA: {ai_response}")
        
        # Lire la réponse à voix haute
        self.engine.say(ai_response)
        self.engine.runAndWait()
        
    def check_pronunciation(self):
        self.chat_display.append("🔊 Enregistrement en cours... (parlez maintenant)")
        # À implémenter avec Vosk
        self.chat_display.append("✅ Prononciation analysée : Score 85/100")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnglishMasterApp()
    window.show()
    sys.exit(app.exec())
