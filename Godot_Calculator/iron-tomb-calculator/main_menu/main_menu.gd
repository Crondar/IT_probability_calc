extends Control


var online_id_generated: bool = false
var connection_data_file_path: String = "user://connection_data.json"


func _ready() -> void:
	load_connection_data()


## Saves the text inputs to a json file so when you reopen the program you don't
## need to refill them.
func save_connection_data() -> void:
	var file: FileAccess = FileAccess.open(connection_data_file_path, FileAccess.WRITE)
	var data_dict: Dictionary = {
		"usernames": %PlayerList.player_name_list,
		"host_id": %HostOnlineID.text,
		"relay_ip": %RelayIP.text,
		"relay_port": %RelayPort.value,
	}
	file.store_string(JSON.stringify(data_dict))
	file.close()


## Loads the text inputs from a json file so when you reopen the program you
## don't need to refill them.
func load_connection_data() -> void:
	# Skip if there is no file.
	if not FileAccess.file_exists(connection_data_file_path):
		%PlayerList.player_name_list = [""]
		return
	
	var file: FileAccess = FileAccess.open(connection_data_file_path, FileAccess.READ)
	
	# Get the data from the file.
	var file_contents: String = file.get_as_text()
	if not file_contents:
		return
	var data_dict: Dictionary = JSON.parse_string(file_contents)
	file.store_string(JSON.stringify(data_dict))
	file.close()
	
	%PlayerList.player_name_list = data_dict["usernames"]
	%HostOnlineID.text = data_dict["host_id"]
	%RelayIP.text = data_dict["relay_ip"]
	%RelayPort.value = data_dict["relay_port"]


## Replaces the my_player_data array with one with updated info.
func setup_player_data() -> void:
	var new_player_data_array: Array[PlayerData] = []
	for entry in %PlayerList.player_name_list:
		var new_player_data = PlayerData.new()
		new_player_data.username = entry
		new_player_data.online_id = MultiplayerHandler.peer.online_id
	MultiplayerHandler.my_player_data = new_player_data_array


## Verify that there exists text in the necessary fields, then attempt to host
## and launch the game.
func _on_host_pressed() -> void:
	setup_player_data()
	save_connection_data()
	
	# Basic input validation.
	var warnings: Array[String] = []
	if not %PlayerList.player_name_list:
		warnings.append("Please list at least one username!")
	for i in range(len(%PlayerList.player_name_list)):
		if %PlayerList.player_name_list[i] == "":
			warnings.append("Please enter a username in entry {0}!".format([i + 1]))
	if not online_id_generated:
		warnings.append("Please generate an online ID first!")
	if warnings:
		%Warning.text = "\n".join(warnings)
		%Warning.visible = true
		return
	else:
		%Warning.visible = false
	
	# Create and launch the game.
	MultiplayerHandler.create_game()
	launch_game()


## Launch the game, calling everyone connected to the game to do so too.
func launch_game() -> void:
	MultiplayerHandler.load_game.rpc("uid://b40vamc7r3og0")  # world.tscn


## Verify that there exists text in the necessary fields, then attempt to join
## and launch the game.
func _on_join_pressed() -> void:
	setup_player_data()
	save_connection_data()
	
	# Basic input validation.
	var warnings: Array[String] = []
	if not %PlayerList.player_name_list:
		warnings.append("Please list at least one username!")
	for i in range(len(%PlayerList.player_name_list)):
		if %PlayerList.player_name_list[i] == "":
			warnings.append("Please enter a username in entry {0}!".format([i + 1]))
	if %HostOnlineID.text == "":
		warnings.append("Please enter the host's online ID!")
	if not online_id_generated:
		warnings.append("Please generate an online ID first!")
	if warnings:
		%Warning.text = "\n".join(warnings)
		%Warning.visible = true
		return
	else:
		%Warning.visible = false
	
	# Join and launch the game.
	MultiplayerHandler.join_game(%HostOnlineID.text)
	launch_game()


func _on_connect_to_relay_pressed() -> void:
	save_connection_data()
	
	# Basic input validation.
	var warnings: Array[String] = []
	if %RelayIP.text == "":
		warnings.append("Please enter a Relay IP address!")
	if warnings:
		%Warning.text = "\n".join(warnings)
		%Warning.visible = true
		return
	else:
		%Warning.visible = false
		
	
	%MyOnlineID.text = "Connecting..."
	print("Connecting to", %RelayIP.text, ":", roundi(%RelayPort.value))
	MultiplayerHandler.connect_to_relay(%RelayIP.text, roundi(%RelayPort.value), online_id_callback)


func online_id_callback(id: String) -> void:
	print("Connected!")
	print("Your id is:", MultiplayerHandler.peer.online_id)
	%MyOnlineID.text = id
	online_id_generated = true
	
