print("hello, pie!") #오 주석도 쉽네?

# 예문 따라 쓴 것
languages=['python', 'perl', 'c', 'java']
for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" %lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" %lang)
    else:
        print("should not reach here")