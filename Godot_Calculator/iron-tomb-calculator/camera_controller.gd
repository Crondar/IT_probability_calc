extends Camera3D

# Reference to camera in your scene
@onready var camera = self

# Hexagonal Prism as a StaticBody or MeshInstance with collision enabled
#@onready var prism = $HexPrism

func _input(event):
	if event is InputEventMouseButton:
		#if event.button_index == Input.BUTTON_LEFT and event.pressed:
			var from = camera.project_ray_origin(event.position)
			var to = from + camera.project_ray_normal(event.position) * 1000
			var space_state = get_world_3d().direct_space_state
			var params := PhysicsRayQueryParameters3D.new()
			params.from = from
			params.to = to
			params.exclude = [camera]
			
			var result = space_state.intersect_ray(params)
			
			if result:
				var collider = result.collider
				var target_position = result.position
				var normal = result.normal

				#if collider == prism:
				#var side_index = get_hex_prism_side(collider, normal)
				print("Clicked on side of ", collider, " at ", target_position, ": ", normal)

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
