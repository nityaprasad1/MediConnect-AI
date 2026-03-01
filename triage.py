def classify_triage(text):
    text = text.lower()

    severe = ["chest pain", "breathing", "seizure", "faint", "unconscious"]
    moderate = ["high fever", "persistent fever", "vomiting", "infection", "swelling"]
    mild = ["cold", "cough", "throat pain", "headache", "body pain", "mild fever"]

    for word in severe:
        if word in text:
            return "severe"

    for word in moderate:
        if word in text:
            return "moderate"

    for word in mild:
        if word in text:
            return "mild"

    return "unknown"