import math

def	is_in_rectangle(w, h, x, y, px, py):
	if px < x or py < y:
		return False
	if px > x + w or py > y + h:
		return False
	return True

def	is_in_left_circle(w, h, x, y, px, py):
	distance = math.sqrt((x - px) ** 2 + (y + h / 2 - py) ** 2)
	if distance <= h / 2:
		return True

def	is_in_right_circle(w, h, x, y, px, py):
	distance = math.sqrt((x + w - px) ** 2 + (y + h / 2 - py) ** 2)
	if (distance <= h / 2):
		return True

w, h, x, y, players = map(int, input().split())
result = 0
for _ in range(players):
	px, py = map(int, input().split())
	if is_in_rectangle(w, h, x, y, px, py):
		result += 1
	elif is_in_left_circle(w, h, x, y, px, py):
		result += 1
	elif is_in_right_circle(w, h, x, y, px, py):
		result += 1
print(result)
