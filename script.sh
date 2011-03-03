#!/bin/sh
#
###########################################################################################
# This Script is going to provide a easy and interactive way to admininstrate a Subversion
# server for any one that needs a SSH access with a defined and logical structure. (Or at 
# least it will pretend to be so) 
#
# It's basis are to have a jerarchy of folders, with infinite levels and infinite branches
# having the subversion repos always in the lower positions in the subdirs.
#
###########################################################################################




# To execute this script, the user will have to be related to any of the subversion groups 
# Para ejecutar este Script, deberá pertenecer a un grupo relacionado con subversion, y 
# dependiendo de a que grupo pertenezca, se le asignarán unos poderes u otros.
# Por tanto, lo primero será saber quien nos está ejecutando
