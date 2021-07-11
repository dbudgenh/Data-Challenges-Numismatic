# For a detailed project report, click [here](https://github.com/dbudgenh/Data-Challenges-Numismatic/blob/master/Report_final.pdf)

# To run the complete code, it is important to install the needed libraries.

1. Start by installing tensorflow. `pip install tensorflow==2.3`
2. Clone the github repository [labelImg](https://github.com/tzutalin/labelImg) into the main directory. Make sure you follow all the steps provided in the repository.
3. Create a new directory, call it Tensorflow/
4. Switch to the directory Tensorflow
5. Clone the [Model Garen Repo](https://github.com/tensorflow/models) into the directory Tensorflow/
6. Create a new directory in the directory Tensorflow/, call it protoc/
7. Install [Protobuf](https://github.com/protocolbuffers/protobuf/releases) and extract it in the just created folder
8. You should now have 2 folders in the directory Tensorflow (models/ and protoc/)
9. Make sure you are in the Tensorflow directory and run the command `protoc/bin/protoc models/research/object_detection/protos/*.proto
--python_out=.` to compile all proto files
10. Install COCO API (only needed for evaluation) by running the command `pip install cython` and `pip install git+https://github.com/philferriere/cocoapi.git`
11. Change directory to Tensorflow/models/research and running the following commands:
12. `cp object_detection/packages/tf2/setup.py .` This will copy the installation file to the current directory
13. `python -m pip install .` This will install it.
14. Test if your installation was succesful by running `python object_detection/builders/model_builder_tf2_test.py`
    

Now you can start preparing the data.

1. Change to the main directory (one folder above Tensorflow)
2. Annotate your images using `python labelImg/labelImg.py`, make sure to place the annotations into the folder workspace/annotations
3. After you are done annotating your images, convert them to tfrecords using `python pascal_xml_to_tfrecords.py`
4. Create a new folder inside workspace, call it pre_trained_models/
5. Go to the [model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md), and select a model you want to work with (e.g EfficientDet D0), extract the model into the pre_trained_models/ folder
6. Inside the workspace/models/ directory, create another directory with with the name of just downloaded model (e.g efficientdet_d0/v1/)
7. From the pre_trained_models/ folder, copy-and-paste the pipeline.config file into this folder.
8. Open the models/efficientdet_d0/pipeline.config file and adjust it to your needs (see this github repo for example)
9. You are now ready to train your network.

# Train your network
cd workspace 
python model_main_tf2.py --pipeline_config_path=./models/efficientdet_d0/v1/pipeline.config --model_dir=./models/efficientdet_d0/v1/ --checkpoint_every_n=10 --num_workers=4 --alsologtostderr

# Log metrics using tensorboard
tensorboard --logdir=workspace/models/efficientdet_d0/v1/train

# Inference (export the model)
python exporter_main_v2.py --trained_checkpoint_dir=./models/efficientdet_d0/v1/ --pipeline_config_path=./models/efficientdet_d0/v1/pipeline.config --output_directory exported_models

# Run inference on the model
python .\inference.py

# Evaluation
python model_main_tf2.py --pipeline_config_path=./models/efficientdet_d0/v1/pipeline.config --model_dir=./models/efficientdet_d0/v1/ --checkpoint_dir=./models/efficientdet_d0/v1/--num_workers=4  --sample_1_of_n_eval_examples=1

# Example
![Example demonstration of coin detection](https://github.com/dbudgenh/Data-Challenges-Numismatic/blob/master/workspace/videos/result_Trim.gif)
