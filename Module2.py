# Production behaviour wise Types:
# 1. Batch Learning
# 2. ⁠Online Learning


# 1. Batch Learning:
#        i. Model is trained in 
#        development environment and 
#        then pushed to production 
#        environment. Generally used 
#       for bigger datasets as training 
#       of such huge datasets over 
#       servers is costly.

#       ii. No Incremental learning 
#           technique is followed. All 
#           datasets are trained 
#           together.

#        Drawbacks:
#        I. Hardware limitations 
#        II. Availablity: process is time 
#            taking.
#        III. Static model
#        IV. Slow

#    Online Learning:
#     i. Initially we have to train our 
#        models over development 
#       environment and then push to 
#       production, then our models 
#       keeps on getting trained 
#       sequentially on smaller batches 
#       of datasets received online.

#    ii. Incremental training of model 
#        is done here.

#    Drawbacks:
#    i. Difficult to use (learning rates, 
#       data processing online,etc.)

#    ii. Risky as chances of model 
#        getting trained by spamming 
#        data.

# Note:
# i.  whenever there is a volatile concept drift ex stock markets we always go for Online learning.
# ii. Else, for simple things like image classification, pattern recognition here we tend to use Batch model.


# Learning Rate: 
# i. How frequently your data is trained. 
# ii. If not a correct learning rate provided then there are the chances model might get trained with new data faster and forget about the old datasets.


# Out Of core learning:
# When we have a bigger datasets in. 
# Development environment then we tend to go for online learning technique and divide the bigger 
# datasets into small chunks and then sequentially send it to model to train it. 
# This is called as Out of core learning.


# On basis of Learning Behaviour:
#   1. Instance based Learning 
#   2. ⁠Model based Learning 

# 1. Instance based Learning: 
#        I. Memorizing (Raatamar)
#        II. No training / learning from 
#            data needed, we just need 
#            to find out similarity based 
#            on datapoints.
#       III. Ex: KNN, RBF networks, 
#            Kernel Functions.
 
    
#     2. Model Based Learning:
#         I. Generalising (Learning 
#            underlying concepts.)
#        II. Training of data is needed in     
#             order to 
#            draw out patterns like a 
#            decision function or a point 
#            to understand underlying 
#            behaviours of datapoints.
#        III. Ex: Linear Regression, 
#             Logistic Regression, 
#             decision trees, etc.