def _check_even_or_odd(int_var):
    out = None
    try:
        if type(int_var) in [int, float]:
            if int_var % 2 == 0:
                out = f"{int_var} is even"
            else:
                out = f"{int_var} is odd"
        elif type(int_var) is str:  # type(int_var) == str
            raise ValueError("type of int_var is str")
        else:
            raise Exception("there is some code error or exception in _check_even_or_odd")
        return out
    except ValueError as e:
        return f"valueError generated, {e}"
    except Exception as e:        
        return f"exception generated, {e}"


if __name__ == "__main__":
    param = [6, 7, 10.00, "indra", {1,2}]

    for i in param:
        out = _check_even_or_odd(int_var=i)
        print(f"param: {i} result: {out}")
