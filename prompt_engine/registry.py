from prompt_engine.naruto import build_naruto_prompt
from prompt_engine.my_hero_academia import build_mha_prompt
from prompt_engine.hunter_x_hunter import build_hxh_prompt

PROMPT_MAP = {
    "naruto": build_naruto_prompt,
    "my hero academia": build_mha_prompt,
    "hunter x hunter": build_hxh_prompt
}

def get_prompt(anime, topic, level, components, character):
    anime = anime.lower()

    if anime not in PROMPT_MAP:
        raise ValueError(f"Anime '{anime}' not supported")

    return PROMPT_MAP[anime](
        topic=topic,
        level=level,
        components=components,
        character=character
    )