from os import system as exc_command

day = int(input("Enter the day: ").strip())
exc_command(f'python -m day_{day}')
