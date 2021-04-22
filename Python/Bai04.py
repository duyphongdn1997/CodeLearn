index_char = lambda x: ord(x) - ord('A') + 1
def number_char(tiles):
  count_char = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in tiles:
    count_char[index_char(i)] += 1
  return backtracking(count_char)

def backtracking(count_char):
  sum = 0
  for i in range(1,27):
    if count_char[i]==0:
      continue
    count_char[i] -= 1
  #  print(count_char)
    sum += 1
    sum+=backtracking(count_char)
    count_char[i] += 1
  #  print("-->",count_char)
  #  print(sum)
  return sum

print(number_char("AAB"))