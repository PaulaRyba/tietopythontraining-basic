def main():
    permissions_definitions = {'read': 'R', 'write': 'W', 'execute': 'X'}

    file_permissions = {}

    for i in range(int(input())):
        file, *permissions = input().split()
        file_permissions[file] = set(permissions)

    for i in range(int(input())):
        operation, file = input().split()
        if permissions_definitions[operation] in file_permissions[file]:
            print('OK')
        else:
            print('Access denied')


if __name__ == '__main__':
    main()
