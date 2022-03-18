---
title: XAI

description: "We work toward XAI. Data Augmentation and Saliency Map Visualization are our research thrusts now"

# image:  img/project-image/XAI-emoji.jpeg
layout: default
last-updated: 2021-09-01

---


- XAI

- Introduction 

At present, the machine learning systems, which has obtained great success and wide application, can provide a certain number of modal data inputs to train the network, and then the model prediction obtains the correct or ideal decision output. This ``end-to-end'' decision-making mode leads to very weak explanatory power of the deep learning model. So,the purpose of explainable technique research is to break this ``black box''  problem and solve various problems caused by it (such as safety problems, bias problems, etc.). Explanation is also one of the development directions of the AI industry in the future. We hope that users can understand and trust the decisions from machine, even if they do not know the specific complex details of the model implementation. 

<img src="/img/project-image/XAI/XAI1.png" alt="XAI1" style="zoom:70%;" />

As we known, it is a long-term study to understand the intrinsic details of models in order to promote human learning and meet human curiosity. Explanation helps to ensure that sensitive information is protected in data privacy and security indicators,  establish trust between humans and models in applications with high performance requirements, so that decisions given by systems more acceptable to domain experts and users.At the technical level, it is also helpful to analyze whether the classifier has biases such as humanistic color through explanation techniques, so as to ensure the fairness and reliability of model decision-making (such as judging classification based on the absence of ethnic skin color). Through a good explanation, experts can explore the root cause of the model’s performance and acquire the internal hidden knowledge. Alternatively, explanation promotes the robustness of networks by emphasizing the potentially antagonistic perturbations that may alter predictions, ensuring that there is a true causal relationship in model inference, and so on. In areas of high risk,it also has important practical application significance in different directions such as military,  life and industry. 

- M-Rules based on DTD

<img src="/img/project-image/XAI/formula.png" alt="FORMULA" style="zoom:70%;" />

we first obtain the decision ``heatmap'' of the training model by changed Deep Taylor Decomposition (DTD) method on the sample data, which called ``M-Rules'',and we verify the performance improvement by comparing evaluation (AOPC or POMPOM) values on Imagenette dataset with others algorithms.Then combine the sample data with the ``heatmap'' by replacing the regions that contribute more to each image return model for training. This can be an iterative process to improve the accuracy of the model.We evaluate the proposed method empirically on the ILSVRC datasets, which highlight the most relevant pixels for the application of decision-making models. 

<img src="/img/project-image/XAI/exp2.png" alt="AOPC" style="zoom:70%;" />

Visualizing the features:Compare the visualization characteristics “heatmap” of the two methods.The first column is the original input image, the middle column is the previous Z-Rule, and the last column is M-Rule proposed in this article.

<img src="/img/project-image/XAI/exp3.png" alt="VISUALIZE" style="zoom:70%;" />


