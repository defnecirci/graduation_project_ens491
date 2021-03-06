# Machine Learning for more efficient SCM processing

Welcome to the GitHub repository for my graduation project's public website!

Modeling the strength behavior of supplementary cementitious materials (SCM) is not straightforward as it is a function of many parameters. The main challenge is the broad variability in the phase composition of the raw materials. Machine learning (ML) methods based on experimental data are shown to be promising to understand the effect of each parameter on SCM’s compressive strength. Furthermore, ML strength prediction models gave satisfactory results when supported by experimental data. In this study, we will work on the characterization data of SCMs that provide information about their phase composition, heat treatment schedules, and physical properties. The aim is to facilitate the development of recipes for more efficient processing of SCMs.

## Installation


### Python packages

In order to run myapp.py you have to have the following packages installed:

* numpy
* pandas
* streamlit

See also the `requirements.txt` file.
You can install each Python package with

```sh
$ pip install packagename
```

or all with

```sh
$ pip install -r requirements.txt
```

## Usage
Change the current working directory to the location where you want the cloned directory and clone the repository. Then, you can run the python script with streamlit run.
```sh
$ git clone https://github.com/defnecirci/graduation_project_ens491.git
$ cd graduation_project_ens491
$ streamlit run myapp.py
```
OR

You can pass a URL to streamlit run:
```sh
$ streamlit run https://raw.githubusercontent.com/defnecirci/graduation_project_ens491/master/myapp.py
```

## Contributing
Pull requests are welcome.

## Acknowledgment
I would like to thank to my graduation project advisors Prof. Cleva Ow-Yang, Dr. İnanç Arın and Prof. Mehmet Ali Gülgün. I have learned a lot from their experiences about science and life. I am greateful.

## References
[1] Hassannezhad, K. (2020). Activation of Aluminosilicate Materials
