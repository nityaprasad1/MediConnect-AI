EMERGENCY_KEYWORDS = [
    "chest pain",
    "breathing difficulty",
    "breathless",
    "seizure",
    "fainting",
    "unconscious",
    "severe bleeding"
]

PRESCRIPTION_KEYWORDS = [
    "antibiotic",
    "amoxicillin",
    "azithromycin",
    "steroid",
    "injection",
    "insulin",
    "painkiller injection"
]

def check_emergency(text):
    text = text.lower()
    for word in EMERGENCY_KEYWORDS:
        if word in text:
            return True
    return False

def check_prescription_request(text):
    text = text.lower()
    for word in PRESCRIPTION_KEYWORDS:
        if word in text:
            return True
    return False