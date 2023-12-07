'''
--- Part One ---

The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last 
digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---

Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
What is the sum of all of the calibration values?'''

with open('d:\\python\\AOC_input_1.txt', 'r') as file:
    all_strings = file.readlines()


def sum_of_the_calibration_values(all_strings):
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0
    for string_with_numbers in all_strings:
        temp_sum = ''
        for left_num in string_with_numbers:
            if left_num in list_of_numbers:
                temp_sum += left_num
                break
        for right_num in string_with_numbers[::-1]:
            if right_num in list_of_numbers:
                temp_sum += right_num
                break
        counter += int(temp_sum)
    print(counter)

def sum_of_the_calibration_values_with_spell(all_strings):
    counter = 0
    list_of_substring = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dict_of_int = {'one' : '1','two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    dict_of_substring_occurrences = {}
    for string_with_numbers in all_strings:
        for spell in list_of_substring:
            if spell in string_with_numbers:
                dict_of_substring_occurrences[spell] = string_with_numbers.find(spell)
        min_index = min(dict_of_substring_occurrences, key = dict_of_substring_occurrences.get)
        max_index = max(dict_of_substring_occurrences, key = dict_of_substring_occurrences.get)
        result_dict = {min_index: dict_of_substring_occurrences[min_index], max_index: dict_of_substring_occurrences[max_index]}
        print(result_dict)
        temp_num = ''
        for key, value in result_dict.items():           
            if len(key) > 1:
                temp_num += dict_of_int.get(key)
            else:
                temp_num += key
        counter += int(temp_num)
        print(counter)

sum_of_the_calibration_values(all_strings)
sum_of_the_calibration_values_with_spell(all_strings)