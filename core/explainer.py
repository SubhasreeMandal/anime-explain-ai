import subprocess
from prompt_engine.registry import get_prompt
from core.concept_mapper import decompose_topic

OLLAMA_PATH = "C:\\Users\\SUBHASREE\\AppData\\Local\\Programs\\Ollama\\ollama.exe"

def explain(topic: str, anime: str, level="beginner", character="Naruto"):
    components_prompt = decompose_topic(topic)

    # LLM Call 1 — Concept extraction
    process1 = subprocess.Popen(
        [OLLAMA_PATH, "run", "phi"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    components, _ = process1.communicate(components_prompt)

    # Build anime-specific prompt
    final_prompt = get_prompt(anime, topic, level, components, character)

    # LLM Call 2 — Explanation
    process2 = subprocess.Popen(
        [OLLAMA_PATH, "run", "phi"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    explanation, _ = process2.communicate(final_prompt)

    return explanation