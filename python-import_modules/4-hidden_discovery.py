#!/usr/bin/python3

import py_compile

if __name__ == "__main__":
    import hidden_4
    module_attributes = dir(hidden_4)
    for name in sorted(module_attributes):
        if not name.startswith("__"):
            print(name)
