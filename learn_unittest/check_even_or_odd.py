def _check_even_or_odd(int_var):
    if int_var % 2 == 0:
        return f"{int_var} is even"
    else:
        return f"{int_var} is odd"


if __name__ == "__main__":
    param = 6
    out = _check_even_or_odd(int_var=param)
    print(f"out: {out}")
