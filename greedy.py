def greedy(data):
	number_libraries = data["lib_amount"]

	process_times = []

	for x in range(number_libraries):
		process_times.append((data[str(x)]["process"], x))