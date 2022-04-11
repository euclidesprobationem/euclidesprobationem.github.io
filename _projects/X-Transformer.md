---
title: X-Transformer

description: "We work toward X-Transformer. As we all know, transformer is SOTA of nlp tasks and generally replace CNN in vision tasks, but the theory about transformers develops a bit slowly, we try to explain and design new attention mechanism by leveraging the rich literatures of differential equation"

# image:  img/project-image/X-transformer/vector_field.png
layout: default
last-updated: 2022-01-02
---

X-Transformer try to connect transformer structure with neural odes, which hints us to treat attention mechanism as a elements in functional space. Previous researches have revealed error controls from numerical methods, Fourier transforms and Galerkin methods from PDE research can indeed improves attention blocks performance, we believes that better structures can be designed with the help with existing mathematics literatures

- Neural ODE - Transformer Progamme


<p align="center">
    <img src="/img/project-image/X-transformer/Neural_ODE_Transformer_Program.png" alt="Neural_ODE_Transformer_Program" style="zoom:70%;" />
</p>

- [Road to Fourier, Galerkin Transformer](https://changhaowu.github.io/2021/12/25/Frequency-Fourier-Galerkin/)

