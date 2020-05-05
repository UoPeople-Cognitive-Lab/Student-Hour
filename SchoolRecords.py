# A function that counts the number of items in a list


def CountNumberOfStudents(CSStudents):
    return len(CSStudents)


def main():
    CS = ['A', 'B', 'C', 'D', 'E']

    return CountNumberOfStudents(CS)


if __name__ == "__main__":
    result = main()
    print(f'The number of students is {result}')
