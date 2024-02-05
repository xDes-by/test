def process_numbers(line):
    numbers = map(int, line.split())
    doubled_numbers = map(lambda x: x * 2, numbers)
    return doubled_numbers


def main():
    with open('data.txt', 'r') as input_file:
        lines = input_file.readlines()

    processed_data = []
    for line in lines:
        doubled_numbers = process_numbers(line)
        processed_data.extend(doubled_numbers)

    average_value = sum(processed_data) / len(processed_data)

    with open('output.txt', 'w') as output_file:
        output_file.write(f'Average value: {average_value}')


if __name__ == "__main__":
    main()
