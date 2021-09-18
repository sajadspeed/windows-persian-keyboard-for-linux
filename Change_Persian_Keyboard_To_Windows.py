changes = [
	{
		"original": "key <BKSL> { [ backslash,		bar,			0x1002010	] };",
		"replace": "key <BKSL> { [ 0x100067e,		bar,			0x1002010	] };",
		"description": "'پ' Character to '\\' key",
		"success": False # Do not change
	},
	{
		"original": "key <AB07> { [ Arabic_peh,		Arabic_hamza,		ellipsis	] };",
		"replace": "key <AB07> { [ Arabic_hamzaonyeh,		Arabic_hamza,		ellipsis	] };",
		"description": "'ئ' Character to 'm' key",
		"success": False # Do not change
	},
	{
		"original": "key <AD05> { [ Arabic_feh,		Arabic_damma,		VoidSymbol	] };",
		"replace": "key <AD05> { [ Arabic_feh,		Arabic_comma,		VoidSymbol	] };",
		"description": "'،'(کاما) Character to 'f' key second level(Shift+f)",
		"success": False # Do not change
	}
]

path = "/usr/share/X11/xkb/symbols/ir"

print("\n  ! Be sure to back up your 'Persian Symbols' file !  \n")
print("Enter or choose path of your 'Persian keyboard symbols' file:")
print("  1. /usr/share/X11/xkb/symbols/ir - Default in (Debian base, Fedora, etc)")
command = input("  ")
if command != '1':
	path = command

try:
	configFile = open(path, "rt")	
	print("\nChanging keyboard layout...\n")
	configFileData = configFile.read().splitlines()

	for i, line in enumerate(configFileData):
		for j, option in enumerate(changes):
			if line.replace(" ", "") == option['original'].replace(" ", ""):
				configFileData[i] = option['replace']
				changes[j]['success'] = True
			if line.replace(" ", "") == option['replace'].replace(" ", ""):
				changes[j]['success'] = True

	configFile.close()

	configFile = open(path, "wt")

	with configFile as f:
		for line in configFileData:
			f.write("%s\n" % line)

	configFile.close()

	allDone = True
	for option in changes:
		if option['success'] == True:
			print(" +",option['description'], "Done...")
		else:
			print(" -",option['description'], "Field!")
			allDone = False

	if allDone:
		print("\nAll done...")
		print("Please login again to make changes.")
	else:
		print("\n! For failed options, check your Persian symbols file and try again. For successful changes login again.")

except NameError:
	print(NameError)
