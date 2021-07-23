n = int(input())
x_coords = []
y_coords = []
for x in range(n):
  input_1, input_2 = input().split(",")
  x_coords.append(int(input_1))
  y_coords.append(int(input_2))



min_x = min(x_coords)
max_x = max(x_coords)
min_y = min(y_coords)
max_y = max(y_coords)

print(min_x-1, min_y-1)
print(max_x+1, max_y+1)
