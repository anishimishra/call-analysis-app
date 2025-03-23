import openai

def llm_compliance_check(conversation):
    prompt = f"""
You are a compliance checker for debt collection calls.
Identify if the following conversation violates compliance by asking personal information like SSN, DOB, or Address.

Conversation:
{conversation}

Reply only 'Yes' if it violates compliance, or 'No' if compliant.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    reply = response['choices'][0]['message']['content'].strip()
    return reply