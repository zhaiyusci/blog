Title: How to set up jupyter notebook on Linux Mint
Date: 2019-06-21 22:30
Category: Technology
Authors: Yu Zhai

Why I need to write this?

The simple answer is that jupyter notebook prefer python3 while 
the newest version of Linux Mint need python2.

I have to admit that I am not a serious python user.
However, I do suggest the python community think about 2to3 problem.
As a lot of people said, py3 should be treated as a totally new language.
Hence, STOP CALL IT PYTHON!

If you follow the installation suggestion following 
[the instruction on the official page](https://jupyter.org/install.html),
and install Anaconda3 following the installation shell script,
you will find your system python is changed to py3.

You are not going to like this change after you open some software like 
Inkscape.  You cannot even copy and paste because of the wrong python.
You can follow 
[this page](https://stackoverflow.com/questions/52046845/changing-the-python-interpreter-for-inkscape) for a solution.

But it is a problem caused by python3, isn't it?  
We do need a way to install py3 without changing the default python behaviour.

Here is the tips.

1. Install miniconda2/3 via script.  Anaconda should be also okay, but I am tired of the big package.
Follow all the instructions include the changing bashrc part.
2. Open your `~/.bashrc` you will going to see this.
```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/miniconda2/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/miniconda2/etc/profile.d/conda.sh" ]; then
        . "/opt/miniconda2/etc/profile.d/conda.sh"
    else
        export PATH="/opt/miniconda2/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
add `conda deactivate` to this part.

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/miniconda2/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/miniconda2/etc/profile.d/conda.sh" ]; then
        . "/opt/miniconda2/etc/profile.d/conda.sh"
    else
        export PATH="/opt/miniconda2/bin:$PATH"
    fi
fi
conda deactivate  # HERE!!!
unset __conda_setup
# <<< conda initialize <<<
```
3. Now you have a brand new miniconda2/3.  That means you now have conda
installed without pollute the system's python.  
Try type `which python` in your terminal to find this (you may want to 
restart your terminal first).

4. Conda is good to manage your python versions.  I install miniconda2
so I need py3.  Type `conda create -n python3 python=3` to create
an "environment" where python3 from Anaconda is the default python.

5. Switch to this environment by `conda activate python3`.  Install the
jupyter notebook by type
```bash
conda install jupyter
conda install pyyaml # I do not know why, but it seems jupyter did not list all its dependences
```
6. Now you have jupyter notebook installed in `python3` environment.  In
our setting, you have to activate the `python3` environment before open the jupyter
notebook.  We simply create a script `jnote` to do this.
```bash
#!/bin/bash

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/miniconda2/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/miniconda2/etc/profile.d/conda.sh" ]; then
        . "/opt/miniconda2/etc/profile.d/conda.sh"
    else
        export PATH="/opt/miniconda2/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

conda activate python3 && jupyter-notebook

```
Put it in a nice place (e.g.,`~/.local/bin` ) and give it the executable
permission and we are good.
