def draw_stars(n):
  if n == 1:
    return ['*']

  stars = draw_stars(n // 3)
  array = []

  for star in stars:
    array.append(star * 3)
  for star in stars:
    array.append(star + ' ' * (n // 3) + star)
  for star in stars:
    array.append(star * 3)
  return array

N = int(input())
print('\n'.join(draw_stars(N)))
