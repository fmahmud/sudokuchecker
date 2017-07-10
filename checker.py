the_input = "934568127826714593157923468278159346641387259395642781563491872789235614412876935"
int_version = []
for character in the_input:
	int_version.append(int(character))

def validate_row(row) :
	sigma = 0
	pi = 1
	for i in range(9) :
		val = int_version[row*9+i]
		sigma += val
		pi *= val
	if pi == 362880 and sigma == 45 : 
		return True
	return False

def validate_col(col) :
	sigma = 0
	pi = 1
	for i in range(9) :
		val = int_version[(i*9)+col]
		sigma += val
		pi *= val
	if pi == 362880 and sigma == 45 : 
		return True
	return False

def validate_box(num) :
	sigma = 0
	pi = 1
	for i in range(9) :
		val = int_version[
				((num%3)*3)+(i%3)+
				((num/3)*27)+(i/3)*9]
		sigma += val
		pi *= val
	if pi == 362880 and sigma == 45 : 
		return True
	print "pi = "+str(pi)+" and sigma = "+str(sigma)
	return False


for i in range(9) :
	if validate_row(i) and validate_col(i) and validate_box(i) :
		print "Valid!"
