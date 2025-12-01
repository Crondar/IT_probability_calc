extends VBoxContainer


const PLAYER_ENTRY = preload("uid://bn1gppr238qg7")

@export var player_name_list: Array: 
	get:
		var return_vals: Array = []
		for child in $Entries.get_children():
			return_vals.append(child.username)
		return return_vals
	set(loaded_values):
		# Balance the number of entry children with the number of values being
		# loaded, either by reproduction or murder.
		var existing_children: int = $Entries.get_child_count()
		for i in range(abs(existing_children - len(loaded_values))):
			if existing_children > len(loaded_values):
				$Entries.remove_child($Entries.get_child(0))
			else:
				add_player_entry()
		# Fill in the values.
		for child in $Entries.get_children():
			child.username = loaded_values.pop_front()


func add_player_entry():
	var new_node = PLAYER_ENTRY.instantiate()
	$Entries.add_child(new_node)


func _on_add_user_pressed() -> void:
	add_player_entry()
