extends Node3D

#func _input(event: InputEvent) -> void:
	#if event.is_action_pressed("ui_up") and MultiplayerHandler.my_id == 1:
		#camera_up.rpc()
		
