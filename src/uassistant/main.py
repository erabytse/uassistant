# src/uassistant/main.py
import sys
import customtkinter as ctk
from .ui import UAssistantGUI
from .utils import ensure_dir, resource_path

def main():
    # Création auto des dossiers
    ensure_dir("./data")
    ensure_dir(resource_path("embedding_model"))
    
    # Thème
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Lancement
    app = ctk.CTk()
    gui = UAssistantGUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()