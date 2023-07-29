def _check_even_or_odd(int_var):
    out = ""
    try:
        if type(int_var) in [int, float]:
            if int_var % 2 == 0:
                out = f"{int_var} is even"
            else:
                out = f"{int_var} is odd"
        else:
            raise ValueError("int_var is not int or float")
        return out
    except ValueError as e:
        return f"valueError generated, {e}"
    except Exception as e:        
        return f"exception generated, {e}"


if __name__ == "__main__":
    param = "indra"
    out = _check_even_or_odd(int_var=param)
    print(f"out: {out}")
