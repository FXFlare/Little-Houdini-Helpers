import hou
import subprocess

def exec_quickbook(framerate, resolution, images_output_dir, video_output_dir, file_name):	
	"""
	This script does write an jpg image sequence from flipbook to disk and does converte this
	sequence to a mov file via ffmpeg.

	Arguments:
		- framerate: Framerate that will be used to write the mov file. Expecting string. E.g.: "25"
		- resolution: Resolution that will be used to write the image sequence and mov file. Expecting string. E.g.: "1920x1080", "1280x720"
		- images_output_dir: Expecting string. E.g.: "C:/Some/Folder/You/Choose/"
		- video_output_dir: Expecting string. E.g.: "C:/Some/Folder/You/Choose/"
		- file_name: The name for your image and video files WITHOUT file extension. Expecting string. E.g.: "Sequ1_Shot01_someName"
	"""

	# Input variables
	framerate = framerate
	resolution = resolution
	images_output_dir = images_output_dir
	video_output_dir = video_output_dir
	file_name = file_name
	
	image_files = (images_output_dir + "/" + file_name + ".$F4.jpg").replace("//","/")
	video_file = (video_output_dir + "/" + file_name + ".mov").replace("//","/")
	images_input = (images_output_dir + "/" + file_name + ".%4d.jpg").replace("//","/")
	
	# Get Houdini viewport class
	desktop = hou.ui.curDesktop()
	scene_viewer = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
	viewport = hou.SceneViewer.curViewport(scene_viewer)

	# Copy the viewer's current flipbook settings
	flipbook_options = scene_viewer.flipbookSettings().stash()

	# Change the flipbook settings
	flipbook_options.output(image_files)

	# Generate the flipbook using the modified settings
	scene_viewer.flipbook(viewport, flipbook_options)
	print "------> image sequence writen to " + images_output_dir

	# Convert image sequence to movie file via ffmpeg
	command = "ffmpeg -f image2 -y -i " + images_input + " -vcodec prores -r " + framerate + " -s " + resolution + " " + video_file
	pipe = subprocess.Popen(command, stdout = subprocess.PIPE)
	pipe.wait()
	print "------> video file writen to " + video_output_dir