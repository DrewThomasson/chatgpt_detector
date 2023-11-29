# chatgpt_detector
Finding ways to detect if its a person writing or if its chatgpt using samples of their writing as input, makes use of the open api and ML

Currently a project Im working on for school

Inspired by this paper in an attempt to create a locally run gpt paper decteor with minimal inout refrence papers:
https://www.sciencedirect.com/science/article/pii/S2666386423005015?via%3Dihub
attempting to see hwo well a neural network is prefroming at the moment for this task

The results of using an Xgboost model with 20 features as stated in the paper were inconclusive had a 95% accuracy in the training data but when testing on other witing it came up with false posatives and false negative looking into the issue...:

I know that theres got ot be a way to differentiate authors by their writing styles so theres got ot be a away to show it with ML of some kind automatically.


![image](https://github.com/DrewThomasson/chatgpt_detector/assets/126999465/91dfdc98-473f-48a7-88c4-eee601f95674)

![image](https://github.com/DrewThomasson/chatgpt_detector/assets/126999465/f3b19ecb-bc8f-45fb-8887-d937cbbcbda6)

