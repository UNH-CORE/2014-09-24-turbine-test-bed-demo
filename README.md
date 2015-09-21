# TurbineDAQ project template

This repo is a template for an experiment automated with [TurbineDAQ](https://github.com/petebachant/TurbineDAQ).


## Installing dependencies

This process assumes the
[Anaconda](http://continuum.io/downloads) or
[Miniconda](http://conda.pydata.org/miniconda.html)
Python packages are installed.

Packages available via `conda`:

    conda install --file requirements-conda.txt

Packages available via `pip`:

    pip install -r requirements-pip.txt


## Creating a new project

First, create a new repository on GitHub, but **do not** add `LICENSE`,
`.gitignore` or `README.md`.

Next, clone the TurbineDAQ project template to your local machine:

    git clone https://github.com/petebachant/TurbineDAQ-project-template.git {your-project-name-here}

Rename the template's remote name:

    git remote rename origin template

Point `origin` to your GitHub repo:

    git remote add origin {your-project-clone-URL}

Updates from the template can then be incorporated with

    git pull template master


## How to use this repository

To create figures and/or tables, run

    python plot.py

To process raw data, run

    python process.py


## License

Code is licensed under the MIT license. See `LICENSE` for details.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" />
</a><br />All other materials licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"/>
Creative Commons Attribution 4.0 International License</a>.
