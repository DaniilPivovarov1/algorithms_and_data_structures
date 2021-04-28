for i in range((127 - 32) // 10 + 1):
    for j in range(32, 128, 10):
        if j + i > 127:
            continue
        print(f'{j + i}-{chr(j + i)}', end='\t')
    print()
