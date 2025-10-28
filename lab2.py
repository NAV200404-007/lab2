def display_main_menu():
    """
    Show instructions to the user.
    Lab says to display:
    "Enter some numbers separated by commas (e.g. 5, 67, 32)"
    """
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    """
    1. Read from console a sequence of numbers separated by commas.
    2. Split by ',' into a list of strings.
    3. Convert that list of strings into a list of floats.
    4. Return the list of floats.

    This matches Table 4 in the lab. :contentReference[oaicite:8]{index=8}
    """
    raw = input("Your input: ")

    # Step 2: split into list of strings
    parts = raw.split(",")

    # Step 3: convert each trimmed string to float
    num_list = []
    for p in parts:
        p_clean = p.strip()
        if p_clean != "":
            num_list.append(float(p_clean))

    # Step 4: return the list of floats
    return num_list


def calc_average_temperature(temp_list):
    """
    Return the average (mean) of all numbers in temp_list.
    Lab Exercise 4 describes this. :contentReference[oaicite:9]{index=9}
    """
    if len(temp_list) == 0:
        return 0.0
    total = 0.0
    for value in temp_list:
        total += value
    avg = total / len(temp_list)
    return avg


def calc_min_max_temperature(temp_list):
    """
    Return a 2-value list [min_temp, max_temp].
    Lab Exercise 4 says: "return an integer list with 2 values for minimum and maximum temperature."
    We'll just return numbers; if you want int specifically you can cast.
    """
    if len(temp_list) == 0:
        return [None, None]

    current_min = temp_list[0]
    current_max = temp_list[0]

    for value in temp_list:
        if value < current_min:
            current_min = value
        if value > current_max:
            current_max = value

    # If your lecturer insists on integer list you can wrap with int() here.
    return [current_min, current_max]


def calc_median_temperature(temp_list):
    """
    Additional Exercise 6:
    1. Sort the list in ascending order.
    2. Return the median value.
       - If odd length: middle element
       - If even length: average of the two middle elements
    """
    n = len(temp_list)
    if n == 0:
        return None

    sorted_list = sorted(temp_list)

    mid_index = n // 2  # integer division

    if n % 2 == 1:
        # odd length -> middle element
        return sorted_list[mid_index]
    else:
        # even length -> average of the two middle elements
        left = sorted_list[mid_index - 1]
        right = sorted_list[mid_index]
        return (left + right) / 2.0


def main():
    # Banner text from the lab’s example main() in Section 7
    # "ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python" :contentReference[oaicite:10]{index=10}
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    # Step 1: show menu / instruction text
    display_main_menu()

    # Step 2: read list of temperatures from user
    temps = get_user_input()

    # Step 3: calculate stats
    average_temp = calc_average_temperature(temps)
    min_temp, max_temp = calc_min_max_temperature(temps)
    median_temp = calc_median_temperature(temps)

    # Step 4: display results to console
    print("You entered:", temps)
    print("Average temperature:", average_temp)
    print("Minimum temperature:", min_temp)
    print("Maximum temperature:", max_temp)
    print("Median temperature:", median_temp)


# This lets Lab2.py act as the main entry point
# exactly like the lab shows with:
# if __name__ == "__main__": main()  :contentReference[oaicite:11]{index=11}
if __name__ == "__main__":
    main()
