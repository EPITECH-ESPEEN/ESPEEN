import importlib
import time
import sys
import os

INITIAL_TIMEOUT = 60

def main() -> int:
    time.sleep(INITIAL_TIMEOUT)
    output = ""
    status = True

    for test in os.listdir("./tests/"):
        if test.startswith('.') or test.startswith('_'):
            continue
        test_module = importlib.import_module(f"tests.{test[:-3]}")
        (test_status, test_output) = test_module.run()
        print(f"Test {test}:\n{test_output}\n", file=sys.stderr)
        output_color = "\033[32mSuccess\033[0m" if test_status else "\033[31mFailure\033[0m"
        output += f"Test \033[35m{test[:-3]}\033[0m: {output_color}\n"
        if not test_status:
            status = False
            break

    print(output)
    return 0 if status else 1

if __name__ == "__main__":
    sys.exit(main())