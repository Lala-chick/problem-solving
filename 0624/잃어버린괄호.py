ME = input()
ME_no_minus = ME.split('-')

answer = sum(list(map(int, ME_no_minus[0].split('+'))))

for token in ME_no_minus[1:]:
    answer -= sum(list(map(int, token.split('+'))))

print(answer)