def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i = 0
    consonat = 0
    while i<len(s):
        if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="o'":
            consonat +=1
        i+=1
    return len(s)-consonat -1
print(main("CodeschoolUz"))