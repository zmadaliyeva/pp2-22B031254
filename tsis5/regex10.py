from re import sub


def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

print(snake_case('JavaScript'))
print(snake_case('Foo-Bar'))
print(snake_case('foo_bar'))
print(snake_case('--foo.bar'))
print(snake_case('Foo-BAR'))
print(snake_case('fooBAR'))
print(snake_case('foo bar'))
