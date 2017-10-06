#-------------------------------------------------------------------------------
# Name:        camera
# Purpose:     Functions for get and set camera state, capture photo
#
# Author:      VoRoN
#
# Created:     06.10.2017
# Copyright:   (c) VoRoN 2017
# Licence:     MIT
#-------------------------------------------------------------------------------
import subprocess

DEBUG = False

def capture_and_download_photo(path):
	sub = subprocess.Popen(['gphoto2','--capture-image-and-download','--filename',
								path, '--force-overwrite'],
								stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								shell=False)
	err = sub.stderr.read()
	if DEBUG:
		print err
	
def check_and_close_gvfs_gphoto():
	psA = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE,
											stderr=subprocess.PIPE, shell=False)
	grep = subprocess.Popen(['grep', 'gvfs[d]*-gphoto'], stdin=psA.stdout,
					stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
	gvfs = grep.stdout.readlines()
	if len(gvfs) > 0:
		for item in gvfs:
			psId = int(item.split('?')[0].strip())
			kill = subprocess.Popen(['kill', '-9', str(psId)],
					stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
					
def get_model():
	summary = subprocess.Popen(['gphoto2', '--summary'], stdout=subprocess.PIPE,
											stderr=subprocess.PIPE, shell=False)
	grep = subprocess.Popen(['grep', 'Model:'], stdin=psA.stdout,
					stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
	model = grep.stdout.readlines()[7:]
	return model

def trigger_capture():
	summary = subprocess.Popen(['gphoto2', '--trigger-capture'],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE, shell=False)
	err = summary.stderr.read()
	if DEBUG:
		print err

def get_all_files(filepattern):
	#pattern example /tmp/capt%04n.jpg
	summary = subprocess.Popen(['gphoto2', '--get-all-files', '--filename',
								filepattern, '--force-overwrite'],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE, shell=False)
	err = summary.stderr.read()
	if DEBUG:
		print err
	
def delete_all_files():
	summary = subprocess.Popen(['gphoto2', '--delete-all-files', '--recurse'],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE, shell=False)
	err = summary.stderr.read()
	if DEBUG:
		print err
	
def shedule_capture_image(interval, count=4):
	sub = subprocess.Popen(['gphoto2','--capture-image', '--interval',
							str(interval), '--frames', str(count)],
								stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								shell=False)
	err = sub.stderr.read()
	if DEBUG:
		print err