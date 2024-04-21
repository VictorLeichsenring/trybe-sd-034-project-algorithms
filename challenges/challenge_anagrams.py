def quick_sort_char_list(char_list):
    if len(char_list) <= 1:
        return char_list
    else:
        pivot = char_list[0]
        less = [x for x in char_list[1:] if x <= pivot]
        # less = []
        # for x in char_list[1:]:
        #     if x <= pivot:
        #         less.append(x)
        greater = [x for x in char_list[1:] if x > pivot]
        # greater = []
        # for x in char_list[1:] :
        #     if x > pivot:
        #         greater.append(x)

        return (quick_sort_char_list(less)
                + [pivot] + quick_sort_char_list(greater))


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        sorted_first = ''.join(quick_sort_char_list(
            list(first_string.lower())))
        sorted_second = ''.join(quick_sort_char_list(
            list(second_string.lower())))
        return (sorted_first, sorted_second, False)

    first_string_lower = first_string.lower()
    second_string_lower = second_string.lower()

    sorted_first = ''.join(quick_sort_char_list(list(first_string_lower)))
    sorted_second = ''.join(quick_sort_char_list(list(second_string_lower)))

    is_anagram_result = sorted_first == sorted_second

    return (sorted_first, sorted_second, is_anagram_result)
