text = input()
# text = text.lower()
words = text.split()
print('\n'.join(word for word in words if word.lower().startswith(('https://', 'http://', 'www.'))))
