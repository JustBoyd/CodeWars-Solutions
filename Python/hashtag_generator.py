def generate_hashtag(s):
    
    if s == "":
        return False
    else:
        new_s = "#" + s.strip().title().replace(" ","")
        if len(new_s) > 140:
            return False
        else:
            return new_s
    pass