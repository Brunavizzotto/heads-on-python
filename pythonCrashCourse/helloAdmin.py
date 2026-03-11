hello = ['admin', 'George', 'Janah', 'Eddy', 'Maggie']

current_users = ['George', 'Janah', 'Eddy', 'Maggie', 'Sophie']
new_users = ['Janah', 'Louis', 'Eddy', 'Fred']

for user in hello:
    if user == 'admin':
        print('Hello sir, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} is already taken, please enter a new username.')
    else:
        print(f'{new_user} is available.')