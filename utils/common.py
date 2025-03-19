import base64

def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return not var == 0
    elif (isinstance(var, list)):
        return len(var) > 0
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == "{}".format(var).lower() for c in empty_chars)

def is_empty (var):
    return not is_not_empty(var)

def is_true (var):
    if isinstance(var, bool):
        return var
    false_char = ["false", "ko", "no", "off"]
    return is_not_empty(var) and not any(c == "{}".format(var).lower() for c in false_char)

def is_false (var):
    return not is_true(var)

def is_disabled (var):
    return is_empty(var) or "changeit" in var

def is_enabled(var):
    return not is_disabled(var)

def is_response_ok(code):
    return code >= 200 and code < 400

def is_response_ko(code):
    return not is_response_ok(code)

def is_numeric (var):
    if isinstance(var, int):
        return True
    return is_not_empty(var) and str(var).isnumeric()

def is_not_numeric (var):
    return not is_numeric(var)

def b64_encode (var, empty_value = ""):
    if is_empty(var):
        return empty_value

    return base64.b64encode(var.encode('utf-8')).decode('utf-8')
