import re

def detect_profanity(conversation, profane_words):
    result = {"Agent": False, "Customer": False}
    pattern = re.compile(r'\b(' + '|'.join(profane_words) + r')\b', re.I)
    for utterance in conversation:
        if re.search(pattern, utterance['text']):
            result[utterance['speaker']] = True
    return result