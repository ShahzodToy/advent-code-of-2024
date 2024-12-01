from collections import Counter
with open("input.txt", "r") as file:
		lines = file.read()
		lines = lines.strip().split("\n")

		left_list = []
		right_list = []

		# Step 3: Split each line and append numbers to the respective lists
		for line in lines:
			left, right = map(int, line.split())
			left_list.append(left)
			right_list.append(right)
				
# left_list.sort()
# right_list.sort()
# total = 0
# for left, right in zip(left_list, right_list):
#         total += abs(left - right)

right_counts = Counter(right_list)

similarity_score = 0
for num in left_list:
    similarity_score += num * right_counts[num]

print(similarity_score)