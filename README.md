# ✅ To‑Do List CLI (Python)

A simple terminal‑based To‑Do List application built with Python.  
You can add, mark as done, delete tasks, and save your list between sessions.

---

## 🧩 Features

- Add a mission/task with a priority tag (HIGH / MIDLL / LOW).  
- List all missions, and mark any as done.  
- Delete a single mission or clear the entire list.  
- Data persistence: tasks are saved to a `todolist.pkl` file using `pickle`.

---

## 🚀 How to Run

### 1. Download or clone the project:

``
git clone https://github.com/<your‑username>/<your‑repo>.git
``

``
cd ... ``

## 📦 Installation Guide

| 🖥️ System        | 💻 Install Python & pip                              | 📚 Install Dependencies             |
|------------------|------------------------------------------------------|-------------------------------------|
| 🐧 Ubuntu/Debian | `sudo apt update && sudo apt install python3 python3-pip` | `pip3 install rich`                |
| 🧢 Fedora         | `sudo dnf install python3 python3-pip`                   | `pip3 install rich`                |
| 🍎 macOS (Homebrew) | `brew install python`                                 | `pip3 install rich`                |

> ✅ **Note:** The project uses standard libraries like `pickle`, `os`, and `shutil`, so no extra installation is needed for those.

4. Run the app:

```bash
python "your_script_name.py"
```

For example:

**python "ToDo List CLI.py"**


**📝 Usage Guide**

When you run the script:

You’ll see a menu:

1. Add a Mission  
2. List The Missions  
3. Delete a Mission  
4. Exit


Add a Mission: type your task lines, then type "save" when done, then choose priority: HIGH / MIDLL / LOW.

List The Missions: displays all tasks, shows which are done, and gives you option to mark a mission done by entering its number.

Delete a Mission: shows list, you enter number to delete, or type ALL to delete everything.

Exit: closes the app.

**🛠️ File Info**

todolist.pkl — The file where tasks are stored between runs.

The script uses pickle for storing and retrieving the List object automatically.

**⚠️ Important Note**

When running this script, make sure your terminal supports ANSI colors and you’re on a normal user account — no elevated permissions are required.
If things look blank or not formatted, try a different terminal.

**📬 Feedback & Contributions**

Feel free to open issues or pull requests on GitHub if you’d like to suggest changes or improvements.
