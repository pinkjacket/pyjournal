def main():
    print_header()
    run_event_loop()


def print_header():
    print("---------------------------")
    print("      JOURNAL APP")
    print("---------------------------")


def run_event_loop():
    print("Welcome to the journal, what do you want to do?")
    cmd = None

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd a new entry, e[X]it: ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            list_entries()
        elif cmd == "a":
            add_entry()
        elif cmd != "x":
            print("Sorry, not an option.")

    print("Done, goodbye!")


def list_entries():
    print("Listing...")


def add_entry():
    print("Adding...")


main()