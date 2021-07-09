# To run the complete code, it is important to install the needed libraries.

1. Start by installing tensorflow. pip install tensorflow==2.3
2. Clone the github repository [labelImg](https://github.com/tzutalin/labelImg) into the main directory. Make sure you follow all the steps provided in the repository.
3. Create a new directory, call it Tensorflow/
4. Switch to the directory Tensorflow
5. Clone the [Model Garen Repo](https://github.com/tensorflow/models) into the directory Tensorflow/
6. Create a new directory in the directory Tensorflow/, call it protoc/
7. Install [Protobuf](https://github.com/protocolbuffers/protobuf/releases) and extract it in the just created folder
8. You should now have 2 folders in the directory Tensorflow (models/ and protoc/)
9. Make sure you are in the Tensorflow directory and run the command `protoc/bin/protoc models/research/object_detection/protos/*.proto
--python_out=.`



Make sure you start in the main directory
# Annotate your images
python labelImg/labelImg.py

# Convert them to tfrecords
python pascal_xml_to_tfrecords.py

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
![Example video of coin detection](https://github.com/dbudgenh/Data-Challenges-Numismatic/blob/master/workspace/videos/result.gif)
