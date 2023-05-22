def solution(m, musicinfos):
    answer = ''
    _max = 0
    
    # 실제로 재생된 음에 m이 속해있어야 함
    # step 1: musicinfo 분해 - 분 단위로 만들어서 끝난 시간 - 시작 시간
    # step 2: (시간 // 악보 정보 길이) * 악보 정보 + 악보 정보[:(시간 % 악보 정보 길이)]
    change_dict = dict()
    change_dict["C#"] = "H"
    change_dict["D#"] = "I"
    change_dict["F#"] = "J"
    change_dict["G#"] = "K"
    change_dict["A#"] = "L"
    
    
    for musicinfo in musicinfos:
        start_time, end_time, title, melodyinfo = musicinfo.split(",")
        start_time = 60 * int(start_time.split(":")[0]) + int(start_time.split(":")[1])
        end_time = 60 * int(end_time.split(":")[0]) + int(end_time.split(":")[1])
        total_time = end_time - start_time
        
        melody_split = melodyinfo
        m_split = m
        for key in change_dict.keys():
            melody_split = melody_split.replace(key, change_dict[key])
            m_split = m_split.replace(key, change_dict[key])
        
        total_melody = melody_split * (total_time // len(melody_split)) + melody_split[:(total_time % len(melody_split))]
        
        if m_split in total_melody:
            if _max < total_time:
                _max = total_time
                answer = title
    
        
    if len(answer) == 0:
        return "(None)"
    return answer