import importlib
import time
import sys
import os

INITIAL_TIMEOUT = 0

def main() -> int:
    time.sleep(INITIAL_TIMEOUT)
    output = ""
    status = True

    tests = os.listdir("./tests/")
    tests.sort()
    for test in tests:
        if test.startswith('.') or test.startswith('_') or test.startswith("xxx"):
            continue
        test_module = importlib.import_module(f"tests.{test[:-3]}")
        try:
            (test_status, test_output) = test_module.run()
        except Exception as e:
            test_status = False
            test_output = f"An error occured: {e}"
        print(f"Test {test}:\n{test_output}\n")
        output_color = "\033[32mSuccess\033[0m" if test_status else "\033[31mFailure\033[0m"
        output += f"Test \033[35m{test[:-3]}\033[0m: {output_color}\n"
        if not test_status:
            status = False
            break

    for test in tests:
        if not test.startswith("xxx"):
            continue
        test_module = importlib.import_module(f"tests.{test[:-3]}")
        try:
            (test_status, test_output) = test_module.run()
        except Exception as e:
            test_status = False
            test_output = f"An error occured: {e}"
        print(f"Test {test}:\n{test_output}\n")
        output_color = "\033[32mSuccess\033[0m" if test_status else "\033[31mFailure\033[0m"
        output += f"Test \033[35m{test[:-3]}\033[0m: {output_color}\n"
        if not test_status:
            status = False
            break

    print(output, file=sys.stderr)
    return 0 if status else 1

if __name__ == "__main__":
    sys.exit(main())