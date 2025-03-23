def calculate_overtalk(conversation):
    overtalk_time = 0
    for i in range(len(conversation) - 1):
        if conversation[i]['etime'] > conversation[i + 1]['stime']:
            overtalk_time += conversation[i]['etime'] - conversation[i + 1]['stime']
    total_time = conversation[-1]['etime']
    return (overtalk_time / total_time) * 100

def calculate_silence(conversation):
    silence_time = 0
    for i in range(len(conversation) - 1):
        gap = conversation[i + 1]['stime'] - conversation[i]['etime']
        if gap > 0:
            silence_time += gap
    total_time = conversation[-1]['etime']
    return (silence_time / total_time) * 100