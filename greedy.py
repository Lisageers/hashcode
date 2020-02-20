def greedy(data):
	number_libraries = data["lib_amount"]

	process_times = []

	for x in range(number_libraries):
		process_times.append((data[str(x)]["process"], data[str(x)]))
	
	sorted(process_times, key=lambda tuple_thing: tuple_thing[0], reverse=True)
	
	day_setup = 0
	scanned_books = set()
	libs_setup = []
	libs_scanned = []

	for day in range(data["days"]):
		if day >= day_setup and len(process_times):
			day_setup += process_times[-1][0]
			libs_setup.append(process_times[-1][1])
			process_times.pop()

		for library in libs_setup:
			libs_books = library["books"]
			libs_ship = int(library["shipping"])
			if len(libs_books) >= libs_ship:
				for book in libs_books[-libs_ship:]:
					scanned_books.add(int(book))
			else:
				for book in libs_books:
					scanned_books.add(int(book))
			del library["books"][-libs_ship:]

	total_score = 0

	scores = data["scores"]

	for book in scanned_books:
		total_score += scores[book]

	return total_score