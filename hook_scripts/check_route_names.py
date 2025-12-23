import ast
import sys
import argparse


def check_file(filename):
    """
    parses a python file to check for route naming conventions
    """
    with open(file=filename, mode="r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    errors = []
    for node in ast.walk(tree):
        # include async route handlers as well
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Check if the function has a decorator that looks like a route
            is_route = any(
                (
                    isinstance(dec, ast.Call)
                    and getattr(dec.func, "attr", "")
                    in ["get", "post", "put", "delete", "patch"]
                )
                or (
                    isinstance(dec, ast.Attribute)
                    and dec.attr in ["get", "post", "put", "delete", "patch"]
                )
                for dec in node.decorator_list
            )
            if is_route and not node.name.startswith("route_"):
                errors.append(
                    f"{filename}:{node.lineno}: Function '{node.name}' must start with 'route_'"
                )

    return errors


def main():
    """
    This function is the scripts entry point, it parses command-line arguments, and it processes files
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    all_errors = []
    for filename in args.filenames:
        all_errors.extend(check_file(filename))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
