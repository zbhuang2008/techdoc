# -*- coding: utf-8 -*-
"""Karpathy's Baby Llama

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dU5ezUiSwMFnkK-Ucd7Q_GgJK_cKX5Gx

Exploring Andrej Karpathy's `llama2.c` aka `Baby Llama`

Credit: https://github.com/karpathy/llama2.c

Downloading the smaller model
"""

! wget https://karpathy.ai/llama2c/model.bin -P out

"""Cloning the `llama2.c` repo to get the required files"""

!git clone https://github.com/karpathy/llama2.c

# Commented out IPython magic to ensure Python compatibility.
# %cd llama2.c

"""Compiling the C code with O3 (Refer - https://github.com/karpathy/llama2.c/issues/20)"""

!gcc -O3 -o run run.c -lm

! ./run ../out/model.bin

"""Compiling the C code with Ofast (Refer - https://github.com/karpathy/llama2.c/issues/20)"""

!gcc -Ofast -o run run.c -lm

! ./run ../out/model.bin

!wget https://karpathy.ai/llama2c/model44m.bin -P out44m
!./run out44m/model44m.bin

!./run out44m/model44m.bin

"""Learning the code from ChatGPT Code Interpreter

1. Configuration and Initialization
    - Define structures: Config, TransformerWeights, RunState
    - Allocate memory for RunState and TransformerWeights

2. Read Checkpoint
    - Initialize the transformer weights from a checkpoint file

3. Main Function
    - Read model configuration and weights from a checkpoint file
    - Read vocabulary from a tokenizer file
    - Initialize the RunState

4. Start Loop for Sequence Generation
    - Call the transformer function to get the output logits for the next token
        - Apply attention mechanism, softmax, RMS normalization, etc.
    - Select the next token using sampling or argmax
    - Print out the token
    - Repeat until a sequence of the maximum length is generated

5. Memory Cleanup
    - Deallocate memory for RunState and TransformerWeights

Flow Chart from Code Interpreter

<img src="https://i.imgur.com/ux73Gq4.png" width="400" height="400" />
"""

