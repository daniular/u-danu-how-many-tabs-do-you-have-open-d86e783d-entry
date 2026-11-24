"""How Many Tabs Do You Have Open?

Writes my honest browser tab count, digits only, to
/output/entry.txt. The count is fixed, so every run writes
the exact same bytes.
"""

import os

TAB_COUNT = "113"

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not TAB_COUNT.isdigit() or not 1 <= len(TAB_COUNT) <= 5:
        raise ValueError("tab count must be 1 to 5 digits")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TAB_COUNT)


if __name__ == "__main__":
    main()
