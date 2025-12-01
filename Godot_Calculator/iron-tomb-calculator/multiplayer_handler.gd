#@icon("res://icon.svg")
extends Node

# Autoload named Lobby

# These signals can be connected to by a UI lobby scene or the game scene.
signal player_connected(peer_id, my_player_data)
signal player_disconnected(peer_id)
signal server_disconnected

#const PORT := 7000
#const DEFAULT_SERVER_IP := "127.0.0.1" # IPv4 localhost
var default_relay_ip := "relay.nodetunnel.io"
var default_relay_port := 9998
const MAX_CONNECTIONS := 20

var peer := NodeTunnelPeer.new()

# This contains arrays of the player data classes for every player,
# with the keys being the unique IDs of the computers they're playing on.
var players: Dictionary[int, Array] = {}
var my_id: int = 0

# This is the local player info. This should be modified locally
# before the connection is made. It will be passed to every other peer.
# For example, the value of "name" can be set to something the player
# entered in a UI scene.
var my_player_data: Array[PlayerData] = [PlayerData.new()]

var players_loaded := 0


func _ready() -> void:
	
	
	multiplayer.peer_connected.connect(_on_player_connected)
	multiplayer.peer_disconnected.connect(_on_player_disconnected)
	multiplayer.connected_to_server.connect(_on_connected_ok)
	multiplayer.connection_failed.connect(_on_connected_fail)
	multiplayer.server_disconnected.connect(_on_server_disconnected)


## Run the code to connect to a given relay.
##[br]
##[br] [param ip]: The IP address of the relay you wish ot connect to.
##[br] [param port]: The port of the relay you wish ot connect to.
##[br]
##[br] Warning! May not succeed to unpredictable effects!
func connect_to_relay(ip: String, port: int, connection_callback: Callable) -> void:
	# Connect to the relay server.
	multiplayer.multiplayer_peer = peer
	peer.connect_to_relay(ip, port)
	
	peer.relay_connected.connect(connection_callback)


func join_game(host_id: String) -> void:
	peer.join(host_id)
	
	await peer.joined
	#if address.is_empty():
		#address = DEFAULT_SERVER_IP
	#var error: Error = peer.create_client(address, PORT)
	#if error:
		#return error
	#multiplayer.multiplayer_peer = peer


func create_game() -> Error:
	# Node relay code.
	peer.host()
	await peer.hosting
	# Copy the id to your clipboard.
	DisplayServer.clipboard_set(peer.online_id)
	# Old code
	#var error = peer.create_server(PORT, MAX_CONNECTIONS)
	#if error:
		#return error
	#multiplayer.multiplayer_peer = peer

	players[1] = my_player_data
	player_connected.emit(1, my_player_data)
	return OK


func remove_multiplayer_peer() -> void:
	multiplayer.multiplayer_peer = OfflineMultiplayerPeer.new()
	players.clear()


# When the server decides to start the game from a UI scene,
# do Lobby.load_game.rpc(filepath)
@rpc("call_local", "reliable")
func load_game(game_scene_path: String) -> void:
	get_tree().change_scene_to_file(game_scene_path)


# Every peer will call this when they have loaded the game scene.
@rpc("any_peer", "call_local", "reliable")
func player_loaded() -> void:
	if multiplayer.is_server():
		players_loaded += 1
		if players_loaded == players.size():
			$/root/Game.start_game()
			players_loaded = 0


# When a peer connects, send them my player info.
# This allows transfer of all desired data for each player, not only the unique ID.
func _on_player_connected(id) -> void:
	_register_player.rpc_id(id, my_player_data)


@rpc("any_peer", "reliable")
func _register_player(new_player_data: Array[PlayerData]) -> void:
	var new_player_id: int = multiplayer.get_remote_sender_id()
	players[new_player_id] = new_player_data
	player_connected.emit(new_player_id, new_player_data)


func _on_player_disconnected(id) -> void:
	players.erase(id)
	player_disconnected.emit(id)


func _on_connected_ok() -> void:
	var peer_id = multiplayer.get_unique_id()
	players[peer_id] = my_player_data
	player_connected.emit(peer_id, my_player_data)


func _on_connected_fail() -> void:
	remove_multiplayer_peer()


func _on_server_disconnected() -> void:
	remove_multiplayer_peer()
	players.clear()
	server_disconnected.emit()
