extends Control


var online_id_generated: bool = false
var connection_data_file_path: String = "user://connection_data.json"


func _ready() -> void:
	load_connection_data()



#func _process(_delta: float) -> void:
	#print("Your id is:", MultiplayerHandler.peer.online_id)


## Saves the text inputs to a json file so when you reopen the program you don't
## need to refill them.
func save_connection_data() -> void:
	var file: FileAccess = FileAccess.open(connection_data_file_path, FileAccess.WRITE)
	var data_dict: Dictionary = {
		"username": $VBox/Username.text,
		"host_id": $VBox/HostOnlineID.text,
		"relay_ip": $VBox/RelayIP.text,
		"relay_port": $VBox/RelayPort.value,
	}
	file.store_string(JSON.stringify(data_dict))
	file.close()


## Loads the text inputs from a json file so when you reopen the program you
## don't need to refill them.
func load_connection_data() -> void:
	# Skip if there is no file.
	if not FileAccess.file_exists(connection_data_file_path):
		return
	
	var file: FileAccess = FileAccess.open(connection_data_file_path, FileAccess.READ)
	
	# Get the data from the file.
	var file_contents: String = file.get_as_text()
	if not file_contents:
		return
	var data_dict: Dictionary = JSON.parse_string(file_contents)
	file.store_string(JSON.stringify(data_dict))
	file.close()
	
	$VBox/Username.text = data_dict["username"]
	$VBox/HostOnlineID.text = data_dict["host_id"]
	$VBox/RelayIP.text = data_dict["relay_ip"]
	$VBox/RelayPort.value = data_dict["relay_port"]


## Replaces the PlayerData object with one with updated info.
func setup_player_data() -> void:
	var new_player_data = PlayerData.new()
	new_player_data.username = $VBox/Username.text
	new_player_data.online_id = MultiplayerHandler.peer.online_id
	MultiplayerHandler.player_data = new_player_data


## Verify that there exists text in the necessary fields, then attempt to host
## and launch the game.
func _on_host_pressed() -> void:
	setup_player_data()
	save_connection_data()
	
	# Basic input validation.
	var warnings: Array[String] = []
	if $VBox/Username.text == "":
		warnings.append("Please enter a username!")
	if not online_id_generated:
		warnings.append("Please generate an online ID first!")
	if warnings:
		$VBox/Warning.text = "\n".join(warnings)
		$VBox/Warning.visible = true
		return
	else:
		$VBox/Warning.visible = false
	
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
	if $VBox/Username.text == "":
		warnings.append("Please enter a username!")
	if $VBox/HostOnlineID.text == "":
		warnings.append("Please enter the host's online ID!")
	if not online_id_generated:
		warnings.append("Please generate an online ID first!")
	if warnings:
		$VBox/Warning.text = "\n".join(warnings)
		$VBox/Warning.visible = true
		return
	else:
		$VBox/Warning.visible = false
	
	# Join and launch the game.
	MultiplayerHandler.join_game($VBox/HostOnlineID.text)
	launch_game()


func _on_connect_to_relay_pressed() -> void:
	save_connection_data()
	
	# Basic input validation.
	var warnings: Array[String] = []
	if $VBox/RelayIP.text == "":
		warnings.append("Please enter a Relay IP address!")
	if warnings:
		$VBox/Warning.text = "\n".join(warnings)
		$VBox/Warning.visible = true
		return
	else:
		$VBox/Warning.visible = false
		
	
	$VBox/MyOnlineID.text = "Connecting..."
	print("Connecting to", $VBox/RelayIP.text, ":", roundi($VBox/RelayPort.value))
	MultiplayerHandler.connect_to_relay($VBox/RelayIP.text, roundi($VBox/RelayPort.value), online_id_callback)


func online_id_callback(id: String) -> void:
	print("Connected!")
	print("Your id is:", MultiplayerHandler.peer.online_id)
	$VBox/MyOnlineID.text = id
	online_id_generated = true
	
