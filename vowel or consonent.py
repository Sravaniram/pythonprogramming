ex=str(raw_input())
if (ex.isalpha()):
	if((ex=='a'or ex=='e'or ex=='i'or ex=='o'or ex=='u')or(ex=='A'or ex=='E'or ex=='I'or ex=='O'or ex=='U')):
		print("Vowel")
	else:
		print("Consonent")
else:
	print("invalid")
