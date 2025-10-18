import shutil
import pickle
import os
from datetime import datetime

columns = shutil.get_terminal_size().columns
time = f" ({datetime.now().strftime('%Y-%m-%d %H:%M')})"

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
BLUE = "\033[34m"
GRAY = "\033[90m"

X = "".center(columns, '-')

try:
    with open('todolist.pkl', 'rb') as f:
        List = pickle.load(f)
except FileNotFoundError:
    List = []

for i, item in enumerate(List):
    if not isinstance(item, tuple):
        List[i] = (item, False)

while True:
    print()
    print(GREEN + BOLD + "What Do You want TO DO!!".center(columns, '-') + RESET)
    print(BOLD + "1. Add a Mission" + RESET)
    print(BOLD + "2. List The Missions" + RESET)
    print(BOLD + "3. Delete a Mission" + RESET)
    print(BOLD + "4. Exit" + RESET)
    print()

    print(BOLD + 'ENTER THE NUMBER OR TYPE THE WORD ["ADD"  "LIST"  "DELETE"  "EXIT"]:'.center(columns) + RESET)
    user = input(">>> ")

    if user.lower() == "clear" or user.lower() == "cls":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    if user.lower() == "add" or user == "A" or user == "1":
        print(X)
        print(BOLD + 'Type What u want If U Finish Type "save":'.center(columns) + RESET)
        print()
        task = ""
        while True:
            line = input()

            if line.lower() == "clear" or line.lower() == "cls":
                os.system("cls" if os.name == "nt" else "clear")
                continue

            if line.lower() == "save":
                print()
                print(X)
                print('RATE THE IMPORTNECE IS ["HIGH"  "MIDLL" "LOW"]')
                rate = input(">>> ")
                if rate.lower() == "high" or rate.lower() == "1":
                    task += BOLD + GREEN + " [HIGH]" + time + RESET
                elif rate.lower() == "midll" or rate.lower() == "2":
                    task += BOLD + YELLOW + " [MIDLL]" + time + RESET
                elif rate.lower() == "low" or rate.lower() == "3":
                    task += BOLD + ORANGE + " [LOW]" + time + RESET
                else:
                    task += BOLD + RED + " [NO RATE]" + time + RESET

                List.append((task.strip(), False))
                break
            else:
                task += line + " "

        with open('todolist.pkl', 'wb') as f:
            pickle.dump(List, f)

    elif user.lower() == "list" or user == "L" or user == "2":
        if not List:
            print(BOLD + "\nNO TASKS FOUND".center(columns) + RESET)
        else:
            print(GREEN + BOLD + "Your TO DO LIST:".center(columns, '-') + RESET)
            for i, (make_done, done) in enumerate(List, 1):
                if done:
                    print(f"\n{i}. {GRAY}{make_done} (DONE){RESET}")
                else:
                    print(f"\n{i}. {make_done}")
            print("\nType The Number Of the Line To Make It DONE ")
            print(BOLD + "Press ENTER to Continue...".center(columns) + RESET)
            done = input(">>> ")
            print()
            if done.isdigit():
                num2 = int(done)
                if 1 <= num2 <= len(List):
                    make_done, _ = List[num2 - 1]
                    List[num2 - 1] = (make_done, True)
                    print(BOLD + GRAY + f"Mission {num2} marked as DONE." + RESET)

                    with open('todolist.pkl', 'wb') as f:
                        pickle.dump(List, f)
                else:
                    continue

    elif user.lower() == "delete" or user == "D" or user == "3":
        if not List:
            print(BOLD + "\nNo Tasks Found".center(columns) + RESET)
            continue
        print(BOLD + "\nYour Mission List:")
        print()
        for i, (make_done, done) in enumerate(List, 1):
            if done:
                print(BOLD + f"{i}. {GRAY}{make_done} (DONE){RESET}")
            else:
                print(BOLD + f"{i}. {make_done}")
        print(BOLD + "\nENTER THE NUMBER U WANT TO DELETE OR TYPE (ALL) TO DELETE EVRETHING:" + RESET)
        num = input(">>> ")

        if num.lower() == "clear" or num.lower() == "cls":
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(List):
                remove = List.pop(num - 1)
                print(BOLD + f"\nMission '{remove[0]}' is Deleted" + RESET)

                with open('todolist.pkl', 'wb') as f:
                    pickle.dump(List, f)

        elif num.lower() == "all":
            confirm = input(BOLD + RED + "\nDo you want to Delete all Missions? (Y/N): " + RESET)

            if confirm.lower() == "y" or confirm.lower() == "yes":
                List.clear()
                print(BOLD + RED + "\nAll Missions Deleted".center(columns) + RESET)
                with open('todolist.pkl', 'wb') as f:
                    pickle.dump(List, f)

    elif user.lower() == "exit" or user == "4" or user == "e":
        print()
        print(BOLD + BLUE + "Exiting... Thank You!".center(columns) + RESET)
        break

    else:
        print(BOLD + RED + "\nINVALID INPUT, PLEASE TRY AGAIN." + RESET)