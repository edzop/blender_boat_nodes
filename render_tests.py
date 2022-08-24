# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import os
import math

#from bpyhullgen.hullgen import geometry_helper 
#from bpyhullgen.hullgen import render_helper
#from bpyhullgen.bpyutils import bpy_helper

target_file = os.environ.get("TARGET_FILE")

print("Working file: '%s'"%target_file)

#exec(open(target_file).read())

blend_file = os.path.basename(bpy.data.filepath)
blendfile_without_extension = os.path.splitext(blend_file)[0]

def do_render():

	frameIndex=bpy.context.scene.frame_current

	#bpy.context.scene.render.resolution_x=2560
	#bpy.context.scene.render.resolution_y=1440

	# you can adjust samples and percentage to get higher quality render
	bpy.context.scene.render.resolution_percentage=100

	bpy.context.scene.render.engine="CYCLES"
	bpy.context.scene.cycles.samples=50
	bpy.context.scene.render.film_transparent = True
	bpy.context.scene.render.image_settings.file_format="PNG"

	try:
		render_result = bpy.ops.render.render(animation=False, write_still=False, layer="", scene="")

		
		print("blend file: %s frame %d/%d"%(blendfile_without_extension,frameIndex,bpy.context.scene.frame_end))
		full_output_image_path="unit_tests/output/%s_%002d.png"%(blendfile_without_extension,frameIndex)
		bpy.data.images['Render Result'].save_render(filepath=full_output_image_path)

		print("Saved to: " + full_output_image_path)
	except Exception as e:
			print("Render Failed")
			return False

	print("Render Result %s"%list(render_result))

#backdrop=geometry_helper.make_backdrop()

#render_helper.create_auto_save_nodes(target_file)

for f in range(bpy.context.scene.frame_start,bpy.context.scene.frame_end+1):
	bpy.context.scene.frame_set(f)
	do_render()
