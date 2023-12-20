def print_header(title, width):
    print(title.upper().center(width, " "))
    print_soft_line(width)


def print_soft_line(width):
    print("-" * width)


def print_line(width):
    print(f"+" + "=" * width + "+")


def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing


def menu_text():
    print("  2 | Display members of your party")
    print("  3 | Show available drinks")
    print("  4 | Add a person")
    print("  5 | Add a drink")
    print("  6 | Specify drink preference")
    print("  7 | Display preferences")
    print("  8 | Quit\n")


def create_table(title, data):
    width = get_table_width(title, data)
    width_is_odd = width % 2 == 1

    if (width_is_odd):  # If width is odd number, title is off-centre, this evens width out for perfect centering of title
        width += 1

    print_header(title, width)

    # padding = " " * (width - 1 - len(item))

    for item in data:
        print(" " + item)# + padding)


def clear_and_show_logo():
    os.system("clear")
    greeting_ascii_art


def new_table(title, data):

    field_one, field_two = list(zip(*data.items()))
    width_field_one = len(max(field_one, key=len))
    width_field_two = len(max(field_two, key=len))

    width = table_total_width(title, data)

    if (
        width % 2 == 1
    ):  # If width is odd number, title is off-centre, this evens width out for perfect centering of title
        width += 1

    SPACING = 2

    print_header(title, width)

    for first, second in data.items():
        column_one = " " + first + " " * (width_field_one - len(first)) + " " + "|"
        column_two = " " + second + " " * (width_field_two - len(second))  # + " " + "|"
        print(column_one + column_two)


def table_total_width(title, data):
    longest = len(title)
    additional_spacing = 4

    for item1, item2 in data.items():
        if len(item1 + item2) > longest:
            longest = len(item1 + item2)

    return longest + additional_spacing
