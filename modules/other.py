def normalize(in_str):
    return in_str.replace('[','').replace(']','').replace('\'','').replace('\\n,','\\n')