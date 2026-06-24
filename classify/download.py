from roboflow import Roboflow

rf = Roboflow(api_key="DPkhFhdDgqAlYOMV4aPO")
project = rf.workspace("jeeh").project("apple-f3ujh-r3zdl")
version = project.version(1)
dataset = version.download("yolov5")
