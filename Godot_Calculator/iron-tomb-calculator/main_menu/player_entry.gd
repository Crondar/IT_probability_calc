extends HBoxContainer


var _username = ""
var username: String:
	get:
		return _username
	set(new_username):
		_username = new_username
		$Username.text = _username


func _on_delete_button_pressed() -> void:
	if get_parent().get_child_count() > 1:  # One for self and one for the add button.
		# Get my index for the array removal after.
		queue_free()


func _on_username_text_changed(new_text: String) -> void:
	_username = new_text
