def positive_numbers(lst):
    return [x for x in lst if x > 0]

def format_comma_without_brackets(lst):
    return ", ".join(map(str, lst))

def main():
    list1 = [12, -7, 5, 64, -14]
    list2 = [12, 14, -95, 3]

    positives1 = positive_numbers(list1)
    positives2 = positive_numbers(list2)

    print(f"Input: list1 = {list1} Output: {format_comma_without_brackets(positives1)}")
    print(f"Input: list2 = {list2} Output: {positives2}")

if __name__ == "__main__":
    main()
