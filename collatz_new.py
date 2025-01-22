'''Find Collatz Sequence'''

import matplotlib.pyplot as plt


def collatz(limit):
    '''Main Function'''
    sequence = [limit]
    while limit != 1:
        if limit % 2 == 0:
            limit = limit // 2
        else:
            limit = 3 * limit + 1
        sequence.append(limit)
    return sequence


user_lim = int(input("Enter a limit : "))

x_axis = []
y_axis = []

x2_axis = []
y2_axis = []

print('\n')
longest_sequence = []
HIGHEST_NUMBER = 0
highest_number_sequence = []


for i in range(1, user_lim + 1):
    current_seq = collatz(i)
    if len(current_seq) > len(longest_sequence):
        longest_sequence = current_seq
    if max(current_seq) > HIGHEST_NUMBER:
        HIGHEST_NUMBER = max(current_seq)
        highest_number_sequence = current_seq

    print(f"{i}: {current_seq}")
    print("\n")
    x_axis.append(i)
    y_axis.append(len(current_seq))
    x2_axis.append(i)
    y2_axis.append(max(current_seq))


print('\n')

print(f"The longest Collatz sequence is {
      longest_sequence} for the number {longest_sequence[0]} with a {len(longest_sequence)} digit length\n")
print(f"Higest number in all the sequences is {HIGHEST_NUMBER} for the number {
      highest_number_sequence[0]}")


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.bar(x_axis, y_axis)
ax1.set_xlabel('Numbers')
ax1.set_ylabel('Number of Numbers in Sequence')
ax1.set_title('Number to Sequence Length')

ax2.plot(x2_axis, y2_axis)
ax2.set_xlabel('Numbers')
ax2.set_ylabel('Higest number in the sequence')
ax2.set_title('Number to Highest Number in Sequence')

plt.show()
