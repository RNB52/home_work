s = str('The 1985 World Snooker Championship final was a snooker match played on the weekend of 27–28 April 1985 at the Crucible Theatre in Sheffield, England. It was the final of the 1985 World Snooker Championship between defending world champion Steve Davis and 1979 runner-up Dennis Taylor (both pictured). The best-of-35-frames match was split into four sessions; Taylor was never ahead during the match, but tied at 17–17.')
s_for = str()
s_comprehension = str()
s_replace = str()

for letter in s:
    if letter != 'a':
        s_for += letter

s_comprehension = ''.join([letter for letter in s if letter != 'a'])

s_replace = s.replace('a', '')

index_last = s.rindex('Dennis')

print('FOR - ', s_for)
print()
print('LIST_COMPREHENSION -', s_comprehension)
print()
print('REPLACE - ', s_replace)
print()
print('LAST_STRING - ', s[index_last:])
print()
print("""The 1985 World Snooker Championship final was a snooker match played on the weekend of 27–28 April 1985 at the Crucible Theatre in Sheffield, England. It was the final of the 1985 World Snooker Championship between defending world champion Steve Davis and 1979 runner-up Dennis Taylor (both pictured). The best-of-35-frames match was split into four sessions; Taylor was never ahead during the match, but tied at 17–17.""")
