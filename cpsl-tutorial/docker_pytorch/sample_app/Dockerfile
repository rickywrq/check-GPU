############################################################
# Dockerfile to build scikit-learn images
# Based on Ubuntu
############################################################

#Set base image to Ubuntu
FROM pytorch/pytorch:2.2.1-cuda11.8-cudnn8-runtime



RUN pip install --upgrade pip


# PYTHON DATA SCIENCE PACKAGES
#   * numpy: support for large, multi-dimensional arrays and matrices
#   * matplotlib: plotting library for Python and its numerical mathematics extension NumPy.
#   * scipy: library used for scientific computing and technical computing
#   * scikit-learn: machine learning library integrates with NumPy and SciPy
#   * pandas: library providing high-performance, easy-to-use data structures and data analysis tools
#   * nltk: suite of libraries and programs for symbolic and statistical natural language processing for English
ENV PYTHON_PACKAGES="\
    numpy \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
" 

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir $PYTHON_PACKAGES 
RUN pip install xgboost

################## END INSTALLATION ########################

#Add hello world script
RUN date