def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.

    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    if (current_day and launch_day) > 0:
        days_left = launch_day - current_day
    else:
        days_left = 0
    # if launch day has already happened return 0

    if days_left < 0:
        days_left = 0

    return days_left
