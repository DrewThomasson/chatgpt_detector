# chatgpt_detector
Finding ways to detect if its a person writing or if its chatgpt using samples of their writing as input, makes use of the open api and ML


Inspired by this paper in an attempt to create a locally run gpt paper decteor with minimal inout refrence papers:
https://www.sciencedirect.com/science/article/pii/S2666386423005015?via%3Dihub
attempting to see hwo well a neural network is prefroming at the moment for this task

The results of using an Xgboost model with 20 features as stated in the paper were inconclusive had a 95% accuracy in the training data but when testing on other witing it came up with false posatives and false negative looking into the issue...:
