
n = int(raw_input().strip())
ratings = []
for _ in range(n):
    ratings.append(int(raw_input().strip()))

total = 1
last_candy = 1
last_increasing_or_equal_index = 0
last_increasing_candy = 1

for i in range(1, n):
    # increasing or equal
    if ratings[i] >= ratings[i - 1]:
        current_candy = last_candy + 1
        if ratings[i] == ratings[i - 1]:
            # if equal
            current_candy = 1

        total += current_candy
        last_candy = current_candy
        last_increasing_or_equal_index = i
        last_increasing_candy = current_candy
    # decreasing
    else:
        if last_increasing_or_equal_index != i - 1:
            proposed_current_value = last_candy - 1
        else:
            # first decreasing item
            proposed_current_value = 1

        if proposed_current_value < 1:
            # reached below 0 so we need to increase all previous elements up to (not including) last increasing index
            total_decreasing_item = i - last_increasing_or_equal_index
            total += total_decreasing_item

            last_candy = 1
            # after the increase in last step we might have reached a point where the increasing property is violated
            if i - last_increasing_or_equal_index == last_increasing_candy:
                total += 1
                last_increasing_candy += 1

        else:
            #
            if proposed_current_value >= last_increasing_candy:
                last_increasing_candy += 1
                total += i - last_increasing_or_equal_index + 1
                last_candy = proposed_current_value
            else:
                total += proposed_current_value
                last_candy = proposed_current_value

print total