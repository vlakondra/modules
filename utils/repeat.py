def is_repeat(s: str, letts: list):
    if not s in letts:
        return s.upper()
    
    print("Символ уже вводился")  