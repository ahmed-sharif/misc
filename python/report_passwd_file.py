def print_frequency():
    frequency_dict = {}
    filename="/etc/passwd"
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            parts = line.split(":")
            shell = parts[-1].strip()
            username = parts[0]
            frequency_dict[shell] = frequency_dict.get(shell, 0) + 1

    shells = frequency_dict.keys()
    shells.sort(key=lambda x: frequency_dict[x], reverse=True)

    for shell in shells:
        print shell, frequency_dict[shell]


if __name__ == '__main__':
    print_frequency()

