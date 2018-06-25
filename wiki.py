import wikipedia

pizza = wikipedia.page("Maple")
with open("return.json", 'w') as f:
	f.write("maple = \"{")
	f.write("\\\"title\\\": \\\"Maple\\\",")
	f.write("\\\"summary\\\": \\\"" + pizza.summary.replace("\n", "").replace("\"", "\\\\\\\"").encode('ascii', 'ignore') + "\\\",")
	f.write("\\\"image\\\": \\\"" + pizza.images[0].replace("\"", "\\\\\\\"") + "\\\"")
	f.write("}\"")