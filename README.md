# anime-explain-ai
A tutor that explains any topic by mapping it into an anime universe, characters, and storytelling style.
# 🍥 Explain Like Anime – AI Tutor

An AI-powered tutor that explains complex topics using anime-style metaphors
(Naruto universe, My hero academia, HunterxHunter) to make learning fun and intuitive.

## 🚀 Features
- Explain any topic using anime storytelling
- Beginner & Intermediate difficulty levels
- Runs fully locally (no paid APIs)
- Built with Python, Ollama, and Streamlit

## 🛠 Tech Stack
# anime-explain-ai

A tutor that explains any topic by mapping it into an anime universe, characters, and storytelling style.

🍥 Explain Like Anime – AI Tutor

This repository contains a small local AI tutor that frames explanations using anime worlds (examples: Naruto, My Hero Academia, Hunter x Hunter). The goal is to make abstract topics intuitive by connecting them to scenes, characters, and training-style metaphors.

## 🚀 Features
- Explain topics using an anime's characters and scenes
- Per-anime prompt templates (Naruto, My Hero Academia, Hunter x Hunter)
- Beginner / Intermediate modes
- Runs locally against a local LLM client (e.g., Ollama)

## 🛠 Tech Stack
- Python 3.10+
- Ollama (local LLM runtime - Phi) — optional but recommended for local runs
- Streamlit (UI at `ui.py`)

## 🧠 What I learned 
This project was also an experiment in practical prompt engineering and running LLMs locally. Key lessons:

- Prompt design: create compact, constrained prompts that (a) keep the model in-character, (b) require examples only from the target anime, and (c) explicitly compare the term to concrete scenes/actions.
   - Use short system-like instructions first ("Answer directly. Do not ask clarifying questions.") for deterministic behavior.
   - Add explicit anti-hallucination rules: "Do NOT invent scenes or episode numbers. If unsure, say 'I don't recall a matching scene' and optionally include a clearly labeled hypothetical example."

- Per-anime templates: keep one small prompt-builder per anime under `prompt_engine/` (e.g., `my_hero_academia.py`, `hunter_x_hunter.py`) so you can tune voice and examples per series without cross-contamination.

- Local LLM integration:
   - The `core/explainer.py` currently calls a local LLM client via `subprocess.run` (e.g., `ollama run ...`). Wrap calls with error handling, timeouts, and logging so failures are visible and manageable.

- Latency & tokens: shorter prompts reduce latency and cost. Move long guidelines into shorter, prioritized instructions and prefer structured output templates.

- Reliability: log the exact prompt and the model response during debugging to catch issues like placeholder text or malformed prompts that cause the model to ask questions instead of answering.

- UI/UX: add CLI flags and a `main()` guard in `app.py` so the script is usable both interactively and programmatically (tests / automation).

## ▶ How to run (local)
1. Install Python 3.10+ (recommended).
2. (Optional) Install and configure Ollama if you plan to run models locally.
3. Install Python deps you need, for example:

```powershell
pip install streamlit
# add any other libs you use (none required for minimal prompt testing)
```

4. Run the CLI script (interactive mode):

```powershell
python app.py
```

5. Or run the Streamlit UI (if `ui.py` is present):

```powershell
streamlit run ui.py
```

## Files of interest
- `app.py` — small CLI/interactive runner that calls `core.explainer.explain()`
- `core/explainer.py` — builds prompts and calls the local LLM client
- `prompt_engine/` — per-anime prompt builders (tune these for voice, examples, hallucination guards)
- `ui.py` — optional Streamlit UI

## Next steps & recommendations
- Add unit tests that mock `core.explainer.explain` and validate output structure.
- Move repeated guard-phrases to a small helper so all prompt builders share the same anti-hallucination rules.
- Add structured output (JSON-like) option so downstream code can parse and render components reliably.

