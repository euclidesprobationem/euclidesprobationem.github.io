#### Construct smaller and faster neural network models

#### Applying network prune、knowledge distillation and quantization methods


##### Network pruning
Pruning algorithm is based on the redundancy of neural network, which aims to cut the unimportant neurons in the network. There are mainly two pruning methods, structured pruning and unstructured pruning. Unstructured pruning produces sparse networks, which requires the cooperation of specific underlying hardware. On the contrary, structured pruning does not need. According to the granularity of pruning, structured pruning can also be divided into channel-based、layer -based and neuron-based. 

##### Knowledge distillation
Knowledge distillation was first proposed by Hinton. Its core idea is to build a smaller student model to learn from a large teacher model, and achieve performance close to that of the teacher model.
