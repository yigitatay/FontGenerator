# FontGenerator
A generative deep learning model to produce fonts.

To run the FontGenerator program, run:
    python FontGenerator.py
Make sure that the dependencies are installed (keras, pyqt5, PIL, numpy). Make sure that the pretrained decoder allDataDecoder.h5 is in the same directory as FontGenerator.py script. 

To download fonts from the internet, the python scripts in the downloadFonts folder can be used.

All the scripts necessary to create the dataset are in the dataset_creation folder. The possible datasets to create are:
- Only alphabetical characters (createDatasetOnlyAlpha.py)
- Alphanumeric characters (createDataset64.py)
- Alphanumeric characters and some symbols (createDataset81.py)

Once the dataset is created, removing the dingbats is recommended for better training (dingbats are the fonts with pictures). 

To train the model, the scripts are in the FONTS_VAE notebook. However, since the dataset is too large, I cannot upload it on Github.
Therefore, the dataset need to be created first to train the model.
If you need the training dataset, let me know and I can share it through Drive.

