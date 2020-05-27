terrains = {
	"sea": [1, 18, 9],
	"field": [3, 15, 19, 21],
	"mountain": [2, 7, 10, 20],
	"swamp": [4, 6, 8, 13],
	"plain": [5, 12, 16, 22],
	"forest": [11, 14, 17, 23]
}
markers = {
	"magic": [4, 11, 15, 19],
	"mine": [2, 14, 10, 6],
	"cave": [2, 5, 13, 22]
}
indigens = [3, 4, 5, 11, 13, 16, 17, 19, 22]
nodes = {}
links = [
	(1, 15),
	(1, 2),
	(2, 15),
	(2, 16),
	(2, 3),
	(3, 16),
	(3, 17),
	(3, 5),
	(3, 4),
	(4, 5),
	(5, 17),
	(5, 6),
	(6, 17),
	(6, 19),
	(6, 7),
	(7, 19),
	(7, 8),
	(8, 19),
	(8, 22),
	(8, 23),
	(8, 9),
	(9, 23),
	(9, 10),
	(10, 23),
	(10, 22),
	(10, 11),
	(11, 21),
	(11, 12),
	(12, 21),
	(12, 13),
	(13, 21),
	(13, 20),
	(13, 14),
	(14, 20),
	(14, 18),
	(14, 16),
	(14, 15),
	(15, 16),
	(16, 17),
	(16, 18),
	(17, 18),
	(17, 19),
	(18, 19),
	(18, 20),
	(19, 20),
	(19, 22),
	(20, 21),
	(20, 22),
	(21, 22),
	(22, 23)
]

borders = list(range(1, 16))
borders.append(23)

if __name__ == "__main__":
	#creating terrain
	for key in terrains:
		for id in terrains[key]:
			nodes[str(id)] = {"terrain": key}
			if key == "mountain":
				nodes[str(id)]["defense"] = {"mountain":1}

	#adding markers
	for key in markers:
		print(key)
		for id in markers[key]:
			print("  {}".format(id))
			if "markers" in nodes[str(id)]:
				nodes[str(id)]["markers"].append(key)
			else:
				nodes[str(id)]["markers"] = [key]

	#adding indigens
	for id in indigens:
		if "defense" in nodes[str(id)]:
			nodes[str(id)]["defense"].update({"indigen": 1})
		else:
			nodes[str(id)]["defense"] = {"indigen": 1}

	#adding links
	for link in links:
		for i in range(2):
			if "links" in nodes[str(link[i])]:
				nodes[str(link[i])]["links"].append(str(link[(i+1)%2]))
			else:
				nodes[str(link[i])]["links"] = [str(link[(i+1)%2])]

	#adding borders
	print(borders)
	for id in borders:
		nodes[str(id)].update({"border":True})

	print(len(nodes))
	print(nodes)