# Paper 1
- AI being used in various sectors like Finance, Computing, Healthcare, Agriculture, Music, Space and Tourism
- Small Sample of Free Music Archives
- **Algorithm Used**:
    - Support Vector Classifier: 46%
    - Logistic Regression: 40%
    - Artificial Neural Network: 67%
    - Convolutional Neural Network: 77%
    - Convolutional Recurrent Neural Network: 90%
    - Parallel Convolutional Recuurent Neural Network: 88%
    - Without Ensemble: 73%
    - With Ensemble: 85% (Ada boost)
- Image based Features better than Label based Features
- Can be used by Music Streaming Platform for music categorisation which can be used further for curating the playlists and recommending the user song according to their favored genre.
- **DATASETS**:
    - GTZAN Dataset
    - FMA Dataset
    - Million Song Dataset
- **Features Used**:
    - MFCC
    - Spectral Centroid
    - Spectral Roll off 
    - Spectral Bandwidth
    - Zero Crossing Rate
    - Chroma STFT

# Paper 2
- Spectrograms used to train the model
- **Dataset**:
    - GTZAN
    - AudioSet 2.1 Million songs into 632 annoted classes.
- **Classificatin Methods**:
    - KNN
    - SVC
    - CNN
- Categorical Cross Entropy Loss
- Sigmoid Function for connected layer in CNN architecture and Softmax in last layer to classify since this is a multi class categorical data.
- **Evaluation Metrics**:
    - Confusion Matrix
    - Accuracy
    - 3 Repeated 10 Fold Validation accuracy
    - Training Time

# Paper 3
- **Algorithms Used**: SVC, KNN, Decision Trees, Neural Networks(CNN,ANN)
- Part of Music Information Retrieval
- Characteristics of Music: Harmony, Melody, Rhythm, Timbre, Pace
- Several Signal Degrading Factors like Noise and Distortion. Model could be trained to perform even better when there's noise and distortion
- **Objective**: To classify the genres accurately using the Deep Learning Models and develop a trustworthy and reliable model
- **Evaluation Metrics**: Accuracy, F1 Score, Precision, Recall, Confusion Matrix
- **Results**:
    - Audio Clips of 30 seconds in `.wav` format with sample rate of `22.05KHz` and 16 bits resolution.
    - MFCCs are used.
- **Conclusions & Future Enhancements**:
    - All the MFCCs saved as JSON File. It lowers the dimensionality. Here dimensionality is 13.
    - Built in works with `.wav` format. Can employ on other audio format. *Categorisation of audio format within genre*
    - *Data Augmentation* can lead to better accuracy.

# Paper 4
- **Algorithm Used**: CNN with Adam Optimizer
- **Objective**: To classify the Music into their respective genres and automate the task of music classification.
- **Accuracy**: 73%
- Two Methods:
    - Train a CNN Model on Spectrograms and let the CNN model extract features.
    - Train a model after extracting features from time and frequency domain.
- JSON format used to store the data
# Paper 5
- 

# Paper 6


# Paper 7