def display_main_menu():
  
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
   
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
  
    if len(temp_list) == 0:
        return 0.0
    total = 0.0
    for value in temp_list:
        total += value
    avg = total / len(temp_list)
    return avg


def calc_min_max_temperature(temp_list):
   
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



if __name__ == "__main__":
    main()
