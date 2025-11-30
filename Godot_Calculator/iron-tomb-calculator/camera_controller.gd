extends Camera3D

## A flag indicating the right mouse button is being held down and the screen should move.
var camera_move: bool = false
var sensitivity: float = .005
var min_angle: float = -PI
var max_angle: float = PI

# Hexagonal Prism as a StaticBody or MeshInstance with collision enabled
#@onready var prism = $HexPrism

func _input(event):
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			var from = project_ray_origin(event.position)
			var to = from + project_ray_normal(event.position) * 1000
			var space_state = get_world_3d().direct_space_state
			var params := PhysicsRayQueryParameters3D.new()
			params.from = from
			params.to = to
			params.exclude = [self]
			
			var result = space_state.intersect_ray(params)
			
			if result:
				var collider = result.collider
				var target_position = result.position
				var normal = result.normal

				#if collider == prism:
				#var side_index = get_hex_prism_side(collider, normal)
				print("Clicked on side of ", collider, " at ", target_position, ": ", normal)
		elif event.button_index == MOUSE_BUTTON_RIGHT:
			camera_move = event.pressed
			#if camera_move:
				#Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
				#Input.
			#else:
				#Input.set_mouse_mode(Input.MOUSE_MODE_)
	elif event is InputEventMouseMotion and camera_move:
		rotation.y -= (event.relative.x * sensitivity)
		global_rotation.x -= (event.relative.y * sensitivity)
		global_rotation.x = clamp(global_rotation.x, min_angle, max_angle)
		
		set_camera_rot.rpc(global_rotation)


func _physics_process(delta: float) -> void:
	var camera_delta := Vector3.ZERO
	if Input.is_key_pressed(KEY_UP):
		camera_delta -= Vector3(0, 0, 1).rotated(Vector3.UP, rotation.y)
	if Input.is_key_pressed(KEY_DOWN):
		camera_delta += Vector3(0, 0, 1).rotated(Vector3.UP, rotation.y)
	if Input.is_key_pressed(KEY_LEFT):
		camera_delta -= Vector3(1, 0, 0).rotated(Vector3.UP, rotation.y)
	if Input.is_key_pressed(KEY_RIGHT):
		camera_delta += Vector3(1, 0, 0).rotated(Vector3.UP, rotation.y)
	
	#global_position += camera_delta.normalized() * delta
	set_camera_pos.rpc(global_position + camera_delta.normalized() * delta)


@rpc("any_peer", "call_local", "reliable")
func set_camera_pos(new_position: Vector3) -> void:
	global_position = new_position


@rpc("any_peer", "call_remote", "reliable")
func set_camera_rot(new_rotation: Vector3) -> void:
	global_rotation = new_rotation


## Function that maps the collision normal to a hex prism side
#func get_hex_prism_side(collider: Node3D, normal: Vector3) -> int:
	## Define hex prism face normals in local space
	#var face_normals = [
		#Vector3(1, 0, 0),
		#Vector3(0.5, 0, sqrt(3)/2),
		#Vector3(-0.5, 0, sqrt(3)/2),
		#Vector3(-1, 0, 0),
		#Vector3(-0.5, 0, -sqrt(3)/2),
		#Vector3(0.5, 0, -sqrt(3)/2),
		#Vector3(0, 1, 0),  # Top
		#Vector3(0, -1, 0)  # Bottom
	#]
	#print(typeof(collider))xform_inv(normal)
	#var local_normal = collider.global_transform.basis.
	#var max_dot = -1
	#var selected_face = -1
#
	#for i in range(face_normals.size()):
		#var dot_product = local_normal.dot(face_normals[i])
		#if dot_product > max_dot:
			#max_dot = dot_product
			#selected_face = i
#
	#return selected_face
