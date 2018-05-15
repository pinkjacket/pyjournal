import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print("---------------------------")
    print("      JOURNAL APP")
    print("---------------------------")


def run_event_loop():
    print("Welcome to the journal, what do you want to do?")
    cmd = "EMPTY"
    journal_name = "Default"
    journal_data = journal.load(journal_name)

    while cmd != "x" and cmd:
        cmd = input("[L]ist entries, [A]dd a new entry, e[X]it: ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry, not an option.")

    print("Done, goodbye!")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Journal Entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx+1, entry))


def add_entry(data):
    text = input("Type your entry, and hit Enter when finished: ")
    journal.add_entry(text, data)


main()