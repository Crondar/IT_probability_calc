extends Node
class_name TileMaterial


## Blocks a mech's movement and doesn't act as solid ground or wall.
var solid: bool
## A list of the types of movement and the modifiers applied by being in or
## blocked by it.
var terrain_modifiers: Dictionary[String, Dictionary]

#func make_file():
	#var temp_hardcoded_dict = {
		#"Flat":
		#{
			#"Walk":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Sand":
		#{
			#"Walk":
			#{
				#"Movement": -1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": 0,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -2,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": 0,
				#"Evasion": -1,
				#"Cover": 0,
			#},
		#},
		#"Rocky":
		#{
			#"Walk":
			#{
				#"Movement": -1,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -2,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -1,
				#"Evasion": 1,
				#"Cover": 0,
			#},
		#},
		#"Scree":
		#{
			#"Walk":
			#{
				#"Movement": -3,
				#"Evasion": -2,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -3,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -2,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Ruins":
		#{
			#"Walk":
			#{
				#"Movement": -1,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -1,
				#"Evasion": 2,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -3,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -2,
				#"Evasion": 1,
				#"Cover": 0,
			#},
		#},
		#"Deep Water":
		#{
			#"Walk":
			#{
				#"Movement": -2,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": -1,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Shallow Water":
		#{
			#"Walk":
			#{
				#"Movement": -1,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -1,
				#"Evasion": -2,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -2,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
		#},
		#"Road":
		#{
			#"Walk":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": 1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": 1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": 1,
				#"Evasion": -1,
				#"Cover": 0,
			#},
		#},
		#"Micro-G":
		#{
			#"Walk":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": -1,
				#"Evasion": -2,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Micro-G Debris":
		#{
			#"Walk":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": -1,
				#"Evasion": -1,
				#"Cover": 1,
			#},
			#"Flight":
			#{
				#"Movement": -1,
				#"Evasion": 1,
				#"Cover": 1,
			#},
			#"Infantry":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Micro-G Urban":
		#{
			#"Walk":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": -2,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": -1,
				#"Evasion": 2,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Wheeled":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Tracked":
			#{
				#"Movement": -99,
				#"Evasion": 0,
				#"Cover": 0,
			#},
		#},
		#"Brush":
		#{
			#"Walk":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 1,
			#},
			#"Wheeled":
			#{
				#"Movement": -1,
				#"Evasion": 0,
				#"Cover": 1,
			#},
			#"Tracked":
			#{
				#"Movement": 0,
				#"Evasion": 1,
				#"Cover": 1,
			#},
		#},
		#"Forest":
		#{
			#"Walk":
			#{
				#"Movement": -1,
				#"Evasion": 1,
				#"Cover": 1,
			#},
			#"Jump":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Flight":
			#{
				#"Movement": 0,
				#"Evasion": 0,
				#"Cover": 0,
			#},
			#"Infantry":
			#{
				#"Movement": -1,
				#"Evasion": 2,
				#"Cover": 1,
			#},
			#"Wheeled":
			#{
				#"Movement": -2,
				#"Evasion": -1,
				#"Cover": 1,
			#},
			#"Tracked":
			#{
				#"Movement": -1,
				#"Evasion": 0,
				#"Cover": 1,
			#},
		#},
	#}
	#var file = FileAccess.open(
		#"res://json_resources/terrain_movement_stats.json",
		#FileAccess.WRITE
	#)
	#
	#file.store_string(JSON.stringify(temp_hardcoded_dict, "\t"))
