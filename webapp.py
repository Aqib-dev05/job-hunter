"""The Job Hunter window: the React page in ui/dist, shown by pywebview (GTK + WebKit, or Qt + QtWebEngine).

Run from source:   ./run.sh        (sets everything up the first time)
or by hand:        python -I webapp.py        (build the page once first:  cd ui && npm ci && npm run build)

pywebview needs one GUI toolkit on Linux. The easiest is GTK with WebKit2:
    Debian / Ubuntu:   sudo apt install python3-gi gir1.2-webkit2-4.1
    Fedora:            sudo dnf install python3-gobject webkit2gtk4.1
    Arch:              sudo pacman -S python-gobject webkit2gtk-4.1
Or Qt, which pip can install by itself:   python -m pip install "pywebview[qt]"
When none is there, this file says so in plain words instead of failing with a stack trace.
"""
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backend  # noqa: E402
import bot  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NO_TOOLKIT = ("Job Hunter needs a GUI toolkit for its window, and none was found.\n\n"
              "Easiest (GTK + WebKit):\n"
              "    Debian / Ubuntu:  sudo apt install python3-gi gir1.2-webkit2-4.1\n"
              "    Fedora:           sudo dnf install python3-gobject webkit2gtk4.1\n"
              "    Arch:             sudo pacman -S python-gobject webkit2gtk-4.1\n"
              "  (the virtual environment must see system packages: ./run.sh already does)\n\n"
              "Or Qt:\n"
              "    python -m pip install \"pywebview[qt]\"")


def page():
    """index.html of the built React page, in ui/dist next to the scripts."""
    return os.path.join(HERE, "ui", "dist", "index.html")


def icon_file():
    """The app icon (the same picture the page uses)."""
    return os.path.join(HERE, "ui", "public", "icon.png")


def message(text, title="Job Hunter"):
    """Tell the person something before any window exists: on the terminal, and in a dialog when one can be shown
    (the app is often started from a launcher, where the terminal is invisible)."""
    print(text, file=sys.stderr)
    if not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
        return
    for cmd in (["zenity", "--info", "--no-markup", "--title", title, "--text", text],
                ["kdialog", "--title", title, "--msgbox", text]):
        if shutil.which(cmd[0]):
            try:
                subprocess.run(cmd, timeout=600, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except (OSError, subprocess.TimeoutExpired):
                pass
            return


def desktop_light_theme():
    """True when the desktop uses a light theme (so the window does not flash dark while it loads)."""
    def gsetting(key):
        try:
            r = subprocess.run(["gsettings", "get", "org.gnome.desktop.interface", key], capture_output=True,
                               text=True, timeout=2)
            return r.stdout.strip().strip("'").lower() if r.returncode == 0 else ""
        except (OSError, subprocess.TimeoutExpired):
            return ""
    scheme = gsetting("color-scheme")
    if scheme == "prefer-dark":
        return False
    if scheme == "prefer-light":
        return True
    theme = gsetting("gtk-theme")
    return bool(theme) and "dark" not in theme


def main():
    index = page()
    if not os.path.exists(index):
        message("The Job Hunter window files are missing.\n\nBuild them once:\n"
                "    cd ui\n    npm ci\n    npm run build\n\n(./run.sh does this for you.)")
        return
    try:
        import webview
    except ImportError:
        message("Job Hunter needs the pywebview package to show its window.\n\nInstall it once:\n"
                "    python -m pip install -r requirements.txt")
        return

    api = backend.Api()
    theme = api.prefs()["theme"]
    light = theme == "light" or (theme == "auto" and desktop_light_theme())
    window = webview.create_window(
        f"Job Hunter {bot.VERSION}", index, js_api=api, width=1400, height=880, min_size=(1040, 660), maximized=True,
        background_color="#f3f3f5" if light else "#1b1b1e", text_select=True)
    api._attach(window)
    icon = icon_file()
    try:
        # The local page is served from 127.0.0.1, so the clipboard and other modern browser features work.
        webview.start(http_server=True, debug=os.environ.get("JOBHUNTER_DEBUG") == "1", private_mode=True,
                      icon=icon if os.path.exists(icon) else None)
    except webview.util.WebViewException as e:
        message(f"{NO_TOOLKIT}\n\n({e})")


if __name__ == "__main__":
    main()
