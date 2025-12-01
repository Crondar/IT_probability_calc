extends Node3D

@export var grid_size: Vector2i = Vector2i(1, 1)
@export var default_base_tile_color = Color(0.165, 0.165, 0.165, 1.0)

const HEX_TILE_SCENE: PackedScene = preload("uid://cqac4pqwuikea")

func _ready() -> void:
	build_base_grid()

## Construct the invulnerable baseplate for construction based on the
## [property grid_size].
func build_base_grid() -> void:
	# Clear the old grid if it exists.
	for child in get_children():
		remove_child(child)
	
	# Build anew.
	for x in range(grid_size.x):
		for y in range(grid_size.y):
			# Create and add the tile.
			var new_tile: HexTile = HEX_TILE_SCENE.instantiate()
			add_child(new_tile)
			
			# Place it in the world where it needs to be.
			var x_pos: float = x * .866  ## An offest needed to tile hexagons properly.
			var y_pos: float = y + 0.5 * (x % 2) ## Offsets every other one by half.
			new_tile.transform.origin = Vector3(x_pos, floor((x+y)/5.0), y_pos)
			
			# Give it its initial stats
			new_tile.set_color(default_base_tile_color)
	
