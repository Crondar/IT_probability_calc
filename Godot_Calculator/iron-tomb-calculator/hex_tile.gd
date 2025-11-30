extends StaticBody3D
class_name HexTile

@export var grid_coords := Vector3i(0, 0, 0)

##Sets the color of the tile. Pretty self explanatory...
##color: Color
func set_color(color: Color) -> void:
	var mesh: MeshInstance3D = $HexMesh
	var material: Material = mesh.mesh.surface_get_material(0)
	material.set_albedo(color)
