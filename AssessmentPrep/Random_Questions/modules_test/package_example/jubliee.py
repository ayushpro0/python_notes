def is_jubliee(n):
    str_n = str(n)

    if str_n.startswith("25") and str_n.endswith("25"):
        return "jubliee"
    else:
        return "not jubliee"