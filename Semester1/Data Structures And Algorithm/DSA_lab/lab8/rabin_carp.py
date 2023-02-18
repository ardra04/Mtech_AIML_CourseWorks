#Rabin Karp algorithm matches the hash value of the pattern with the hash value of the current substring of text, 
# and if the hash values match then only it starts matching individual characters.


d = 256                    # d  =  number of characters in the input alphabet
def search(pat, txt, q):   # pat -> pattern , txt -> text , q -> A prime number
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1
	                                                         
	for i in range(M-1):
		h = (h*d) % q                                      # The value of h would be "pow(d, M-1)%q" 
                                              
	for i in range(M):                                     # Calculate the hash value of pattern and first window of text
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(txt[i])) % q
	                                                      
	for i in range(N-M+1):             #  Check the hash values of current window of text and pattern match then only check for characters one by one
		if p == t:
			                                                # Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1
			if j == M:
				print("Pattern found at index " + str(i))

		# Calculate hash value for next window of text
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
			if t < 0:
				t = t+q


if __name__ == '__main__':
	txt = "ABCCDDAEFG"
	pat = "CDD"
	q = 101 
	search(pat, txt, q)      




#Initially calculate the hash value of the pattern.
#Start iterating from the starting of the string and compare hash values
#if not same, slide window.
#if match found, check pattern is same


