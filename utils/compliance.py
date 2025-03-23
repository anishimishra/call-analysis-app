import re

def extract_utterance_text(utterance):
    """
    Safely extracts the text from an utterance, handling potential missing keys.
    """
    return utterance.get('text', '').lower()

def is_sensitive_info(text):
    """
    Checks if the text contains sensitive information.
    """
    balance_pattern = re.compile(r'\b(?:your\s+)?balance(?: is)?\s*(?:[$£¥])?\s*[\d,.]+\b', re.IGNORECASE)
    account_pattern = re.compile(r'\b(?:your\s+)?account(?: number)?(?: is)?\s*\d+\b', re.IGNORECASE)
    return bool(balance_pattern.search(text)) or bool(account_pattern.search(text))

def is_identity_verified(text):
    """
    Checks if the text indicates identity verification.
    """
    dob_pattern = re.compile(r'\b(?:date\s+of\s+birth|DOB)(?: is)?\b', re.IGNORECASE)
    address_pattern = re.compile(r'\baddress(?: is)?\b', re.IGNORECASE)
    ssn_pattern = re.compile(r'\b(?:social\s+security\s+number|SSN)(?: is)?\b', re.IGNORECASE)
    return (
        bool(dob_pattern.search(text))
        or bool(address_pattern.search(text))
        or bool(ssn_pattern.search(text))
    )

def detect_compliance_violation(conversation):
    """
    Detects compliance violations in a conversation by identifying cases where
    agents share sensitive information without prior identity verification.

    Args:
        conversation: A list of dictionaries, where each dictionary represents an utterance
                      and contains keys like 'speaker' and 'text'.

    Returns:
        bool: True if a compliance violation is detected, False otherwise.
    """
    
    violation_occurred = False
    identity_verified = False  # Flag to track if verification happened

    for utterance in conversation:
        speaker = utterance.get('speaker', '').lower()
        text = extract_utterance_text(utterance)

        if is_identity_verified(text):
            identity_verified = True  # Verification occurred

        if speaker == 'agent' and is_sensitive_info(text) and not identity_verified:
            violation_occurred = True  # Violation: sensitive info before verification
            break  # Exit on the first violation

    return violation_occurred