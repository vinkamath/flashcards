import sys
import os
sys.path.append('..')

from kandinsky3 import get_T2I_pipeline


def gen_image(prompt):
	t2i_pipe = get_T2I_pipeline('cuda:0', fp16=True)
	return t2i_pipe(prompt) 