import os.path as path
import sys

script_path = path.abspath(__file__)
__script_dir = path.dirname(script_path)
__script_dir_alt = sys.path[0]
__icon_path = path.join(__script_dir, "favicon.ico")


def center(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")


def ontop(window):
    window.lift()
    window.attributes("-topmost", True)


def main():
    print("")
    print(__script_dir)
    print(__script_dir_alt)
    print(__icon_path)
    print("")
    print("✅ This module is working as intended")


if __name__ == "__main__":
    main()
