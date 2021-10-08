def perm(list):
  if len(list) == 1:
    yield list
  else:
    for i in range(len(list)):
      for p in perm(list[:i] + list[i+1:]):
        yield [list[i]] + p

#print(list(perm(['A', 'B', 'C'])))

pods = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
arrangements = []
for i in range(len(pods)):
  for j in range(i+1, len(pods)):
    for k in range(j+1, len(pods)):
      for l in range(k+1, len(pods)):
        group1 = [pods[i], pods[j], pods[k], pods[l]]
        remaining = pods[:i] + pods[i+1:j] + pods[j+1:k] + pods[k+1:l] + pods[l+1:]
        #print(group1)
        #print(remaining)
        m = 0 # first element of remaining always goes to first group of three
        for n in range(1, len(remaining)):
          for o in range(n+1, len(remaining)):
            group2 = [remaining[0], remaining[n], remaining[o]]
            group3 = remaining[1:n] + remaining[n+1:o] + remaining[o+1:]
            arrangements.append((group1, group2, group3))

#print(len(arrangements))
print('week, ' + 'Group A, '*4 + 'Group B, '*3 + 'Group C, '*3)
print("week 0, " + ", ".join(pods))

invert = {}
for i in range(len(pods)):
  invert[pods[i]] = i

#print(invert)
overlap = [[0 for i in range(10)] for j in range(10)]

def overlaps(a, b):
    return overlap[invert[a]][invert[b]]

def increase_overlaps(groupings):
    group1 = groupings[0]
    group2 = groupings[1]
    group3 = groupings[2]

    overlap[invert[group1[0]]][invert[group1[1]]] += 1
    overlap[invert[group1[0]]][invert[group1[2]]] += 1
    overlap[invert[group1[0]]][invert[group1[3]]] += 1
    overlap[invert[group1[1]]][invert[group1[2]]] += 1
    overlap[invert[group1[1]]][invert[group1[3]]] += 1
    overlap[invert[group1[2]]][invert[group1[3]]] += 1
  
    overlap[invert[group2[0]]][invert[group2[1]]] += 1
    overlap[invert[group2[0]]][invert[group2[2]]] += 1
    overlap[invert[group2[1]]][invert[group2[2]]] += 1

    overlap[invert[group3[0]]][invert[group3[1]]] += 1
    overlap[invert[group3[0]]][invert[group3[2]]] += 1
    overlap[invert[group3[1]]][invert[group3[2]]] += 1

def penalty(groupings):
    penalty = 0
    group1 = groupings[0]
    group2 = groupings[1]
    group3 = groupings[2]

    penalty += overlaps(group1[0], group1[1])**2
    penalty += overlaps(group1[0], group1[2])**2
    penalty += overlaps(group1[0], group1[3])**2
    penalty += overlaps(group1[1], group1[2])**2
    penalty += overlaps(group1[1], group1[3])**2
    penalty += overlaps(group1[2], group1[3])**2

    penalty += overlaps(group2[0], group2[1])**2
    penalty += overlaps(group2[0], group2[2])**2
    penalty += overlaps(group2[1], group2[2])**2

    penalty += overlaps(group3[0], group3[1])**2
    penalty += overlaps(group3[0], group3[2])**2
    penalty += overlaps(group3[1], group3[2])**2
    
    return penalty

def print_overlaps():
    for i in range(len(overlap)):
        print(overlap[i])

increase_overlaps(arrangements[0])

#print_overlaps()
for week in range(1, 50):
  best = arrangements[0]
  best_penalty = penalty(best)
  for i in range(1, len(arrangements)):
    penalty_value = penalty(arrangements[i])
    if penalty_value < best_penalty:
      best = arrangements[i]
      best_penalty = penalty_value
  print("week " + str(week) + ",", ", ".join(best[0]) + ",", ", ".join(best[1]) + ",", ", ".join(best[2]))
  increase_overlaps(best)
  #print_overlaps()


