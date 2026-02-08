def decompose_topic(topic: str) -> list:
    """
    Breaks a topic into core components.
    """
    prompt = f"""
List the key components of the topic "{topic}".
Return ONLY a bullet list.
"""
    return prompt