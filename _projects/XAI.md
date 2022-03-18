---
title: XAI

description: "We work toward XAI. Data Augmentation and Saliency Map Visualization are our research thrusts now"

# image:  img/project-image/XAI-emoji.jpeg
layout: default
last-updated: 2021-09-01

---


- XAI

- Introduction 

At present, the machine learning systems, which has obtained great success and wide application, can provide a certain number of modal data inputs to train the network, and then the model prediction obtains the correct or ideal decision output. This ''end-to-end'' decision-making mode leads to very weak explanatory power of the deep learning model. So,the purpose of explainable technique research is to break this ''black box''  problem and solve various problems caused by it (such as safety problems, bias problems, etc.). Explanation is also one of the development directions of the AI industry in the future. We hope that users can understand and trust the decisions from machine, even if they do not know the specific complex details of the model implementation. 

<img src="/img/project-image/XAI/XAI1.png" alt="XAI1" style="zoom:70%;" />

**- M-Rules based on DTD**

Since the core idea of Taylor decomposition is to decompose the original function by the function at a point so that it is constantly approximated, that is, a point contains the information of the entire function. **The relevance score function has a root point at midpoint**:

<img src="/img/project-image/XAI/formula.png" alt="FORMULA" width="500px" />

we first obtain the decision ''heatmap'' of the training model by changed Deep Taylor Decomposition (DTD) method on the sample data, which called ''M-Rules'',and we verify the performance improvement by comparing evaluation (AOPC or POMPOM) values on Imagenette dataset with others algorithms.Then combine the sample data with the ''heatmap'' by replacing the regions that contribute more to each image return model for training. This can be an iterative process to improve the accuracy of the model.We evaluate the proposed method empirically on the ILSVRC datasets, which highlight the most relevant pixels for the application of decision-making models. 

As base architecture the pretrained AlexNet，our dataset **is a subset of Imagenet and contains ten classes**, which called Imagenette. After 100 or 200 perturbation rounds, each round disturbs a position of information. The experiment calculates the AOPC curves relative to a random baseline for the M-Rules,LRP,deconvolution and sensibility algorithms with norms and variations.
<img src="/img/project-image/XAI/exp2.png" alt="AOPC" width="500px" />

Visualizing the features on the ILSVRC datasets:Compare the visualization characteristics “heatmap” of the two methods.The first column is the original input image, the middle column is the previous Z-Rule, and the last column is M-Rule.

<img src="/img/project-image/XAI/exp3.png" alt="VISUALIZE" width="500px" />


  
