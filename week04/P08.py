def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_t = str_to_sec(video_len)
    pos_t = str_to_sec(pos)
    start_t = str_to_sec(op_start)
    end_t = str_to_sec(op_end)
    
    if (start_t<= pos_t and pos_t <= end_t):
            pos_t = end_t
    
    for i in range(len(commands)):
        if (commands[i]=="prev"):
            if(pos_t < 10):
                pos_t = 0
            else:
                pos_t -= 10
        elif (commands[i]=="next"):
            if (video_t - pos_t < 10):
                pos_t = video_t
            else:
                pos_t += 10
        if (start_t<= pos_t and pos_t <= end_t):
            pos_t = end_t
        
        minute = pos_t // 60
        second = pos_t % 60
        
    return f"{minute:02d}:{second:02d}"

def str_to_sec(string):
    t = string.split(":")
    time = 60*int(t[0]) + int(t[1])
    return time

# datetime 쓰는 방식
# a = datetime.strptime("03:25", "%M:%S")