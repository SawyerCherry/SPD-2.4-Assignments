#instructors

instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_i(arr, name):
    output = []

    def recursive(index):

        if index >= len(arr):
            return

        elif arr[index] == name and len(output) == 0:
            output.append(index)

        elif arr[index] != name and len(output) == 1:
            output.append(index - 1)

        index += 1
        recursive(index)

    recursive(0)
    return output


print(find_i(instructors, 'Braus'))