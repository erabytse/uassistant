# src/uassistant/core.py
"""Cœur métier : détection de langue, prompts, appel Ollama."""
import requests
from typing import Optional

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

PROMPTS = {
    "de": "Sie sind UAssistant, ein professioneller, diskreter Assistent. Antworten Sie präzise und auf Deutsch.",
    "en": "You are UAssistant, a professional, discreet assistant. Respond concisely in English.",
    "fr": "Vous êtes UAssistant, un assistant professionnel et discret. Répondez de façon concise en français."
}

UI_LABELS = {
    "de": {"listen": "🎙️ ZUHÖREN", "send": "📤 SENDEN", "hint": "Frage eingeben...", "thinking": "Denkt nach..."},
    "en": {"listen": "🎙️ LISTEN", "send": "📤 SEND", "hint": "Enter your question...", "thinking": "Thinking..."},
    "fr": {"listen": "🎙️ ÉCOUTER", "send": "📤 ENVOYER", "hint": "Posez votre question...", "thinking": "Réfléchit..."}
}

def detect_language(text: str) -> str:
    """Détection simple par mots-clés (améliorable avec langdetect si besoin)."""
    text_lower = text.lower()
    if any(w in text_lower for w in ["der", "die", "das", "und", "ist", "frage", "antwort"]): return "de"
    if any(w in text_lower for w in ["le", "la", "les", "et", "est", "question", "réponse"]): return "fr"
    return "en"  # fallback

def build_prompt(user_text: str, lang: str, context: Optional[str] = None) -> str:
    system = PROMPTS.get(lang, PROMPTS["en"])
    if context and context.strip():
        return f"{system}\n\nInformations pertinentes:\n{context}\n\nQuestion: {user_text}\nRéponse:"
    return f"{system}\n\nQuestion: {user_text}\nRéponse:"

def ask_ollama(prompt: str, model: str = OLLAMA_MODEL, timeout: int = 120) -> str:
    try:
        resp = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.3}},
            timeout=timeout
        )
        if resp.ok:
            return resp.json().get("response", "Aucune réponse.").strip()
        return "❌ Erreur Ollama."
    except Exception as e:
        return f"❌ Connexion: {str(e)}"