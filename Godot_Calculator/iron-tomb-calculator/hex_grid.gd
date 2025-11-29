extends Node3D

@export var grid_size: Vector2i = Vector2i(1, 1)

const tile_pattern: PackedScene = preload("res://hex_tile.tscn")

func _ready():
	for x in range(grid_size.x):
		for y in range(grid_size.y):
			var new_tile: HexTile = tile_pattern.instantiate()
			add_child(new_tile)
			new_tile.transform.origin = Vector3(x*.866, floor((x*y)/5.0), (y + 0.5 * (x % 2)))
			new_tile.set_color(Color(1.0, 0.0, 0.0, 1.0))
			print("added child at ", new_tile.transform.origin)
