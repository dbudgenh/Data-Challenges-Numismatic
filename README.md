
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

# Example
![Test](\workspace\videos\result.gif)
