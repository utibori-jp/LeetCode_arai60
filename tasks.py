import argparse
import subprocess
import sys
from pathlib import Path

PROBLEMS_DIR = Path(__file__).parent / "problems"


def cmd_test(args):
    problem_dir = PROBLEMS_DIR / args.number
    if not problem_dir.exists():
        print(f"Error: problems/{args.number}/ not found", file=sys.stderr)
        sys.exit(1)
    subprocess.run(["uv", "run", "pytest", str(problem_dir), "-v"])


def cmd_test_all(_args):
    subprocess.run(["uv", "run", "pytest", str(PROBLEMS_DIR), "-v"])


def cmd_run(args):
    solution = PROBLEMS_DIR / args.number / "solution.py"
    if not solution.exists():
        print(f"Error: problems/{args.number}/solution.py not found", file=sys.stderr)
        sys.exit(1)
    subprocess.run(["uv", "run", "python", str(solution)])


def cmd_list(_args):
    dirs = sorted(p for p in PROBLEMS_DIR.iterdir() if p.is_dir())
    if not dirs:
        print("No problems found")
        return
    for d in dirs:
        print(d.name)


def main():
    parser = argparse.ArgumentParser(description="arai60 task runner")
    sub = parser.add_subparsers(dest="command", required=True)

    p_test = sub.add_parser("test", help="run tests for a specific problem")
    p_test.add_argument("number", help="problem number (e.g. 001)")
    p_test.set_defaults(func=cmd_test)

    p_run = sub.add_parser("run", help="run solution.py directly for a specific problem")
    p_run.add_argument("number", help="problem number (e.g. 001)")
    p_run.set_defaults(func=cmd_run)

    p_all = sub.add_parser("test-all", help="run tests for all problems")
    p_all.set_defaults(func=cmd_test_all)

    p_list = sub.add_parser("list", help="list all problems")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
