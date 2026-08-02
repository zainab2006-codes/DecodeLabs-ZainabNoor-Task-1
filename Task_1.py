my_tasks = list()

while True:
    print('------- To-Do List -------\n')
    print('1. Add task')
    print('2. View list of tasks')
    print('3. Exit\n')

    choice = input('Enter choice (1-3): ')

    if choice == '1':
        new_task = input('\nEnter task: ')

        my_tasks.append(new_task)

        print('Task added successfully !\n')

    elif choice == '2':
        if len(my_tasks) == 0:
            print('\nNo tasks  availaible in the list')

        else:
            print('\nYour task list:\n')

            for i , task in enumerate(my_tasks , start=1):
                print(f'{i}. {task}')

            print()

    elif choice == '3':
        print('\nExiting the To-Do List. Have a great day!')
        break

    else:
        print('\nInvalid choice entered !')
        print('Choose between 1-3')