prompt = input("prompt: ")

letters = sorted(set(prompt))

letter_to_num = {}
for num, letter in enumerate(letters):
    letter_to_num[letter] = num

num_to_letter = {}
for letter, num in letter_to_num.items():
    num_to_letter[num] = letter

def encode(output):
    nums = []
    for letter in output:
        nums.append(letter_to_num[letter])
    return nums

def decode(nums):
    output = ""
    for num in nums:
        output = output + num_to_letter[num]
    return output
