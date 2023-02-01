def merge_sort(items):
  # If the input sequence contains 0 or 1 items,
  # it is already sorted, so return it
  if len(items) <= 1:
    return items

  # Split the input sequence into two subsequences
  # and sort each subsequence using the merge_sort() function
  mid = len(items) // 2
  left = merge_sort(items[:mid])
  right = merge_sort(items[mid:])

  # Merge the two sorted subsequences into a single sorted sequence
  result = []
  while left and right:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  result.extend(left if left else right)

  # Return the sorted sequence
  return result

# Define the input sequence
items = [3, 4, 2, 1, 6, 5]

# Sort the sequence using the merge_sort() function
sorted_items = merge_sort(items)

# Print the sorted sequence
print(sorted_items)  # Output: [1, 2, 3, 4, 5, 6]
