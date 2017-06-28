def clockToString(input):
	hours = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
	tens = ["oh", "", "twenty", "thirty", "fourty", "fifty"]
	ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	tentwen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

	h, m = map(int, input.split(":"))
	res = "It's "
	res += hours[h%12] + " "
	if 9 < m < 19: res += tentwen[m-10] + " "
	elif (m % 10) == 0: res += tens[m//10] + " "
	elif (m != 0): res += tens[m//10] + " " + ones[m%10] + " "
	res += "pm" if h//12 else "am"
	return res
	# Horrible looking way to return in one line
	#return "It's {} {}".format("{} {}".format(hours[h%12], "{}".format(tentwen[m-10] if (9<m<19) else "{}".format(tens[m//10]) if (m%10) == 0 else "{} {}".format(tens[m//10],ones[m%10]))) if m else hours[h%12], "pm" if h//12 else "am")

if __name__ == "__main__":
	inputs = ["00:00", "01:30", "12:05", "14:01", "20:29", "21:00"]
	for input in inputs:
		print(clockToString(input))