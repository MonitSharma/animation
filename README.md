# How to Install Manim for Mac?

## Step 1: Make a Virtual Environment

It is a tool that lets you create an isolated Python environment for the project. You can even configure which version of Python you want for your project.

#### Installation

To install `virtualenv` run

```python
pip3 install virtualenv
```


#### Usage

Change to the directory of your project and make the virtualenv there:

```python
cd project
virtualenv venv
```


Activate it using

```python
source venv/bin/activate
```

## Manim on Mac

You should've installed [Homebrew](https://brew.sh/)

then install the **Required Dependencies**

```python
brew install py3cairo ffmpeg
```


some additional dependencies are required

```python
brew install pango pkg-config scipy
```

After all this, simply run
```python
pip3 install manim
```

### Installing Latex
This is important, either download the full 4GB of [MacTex](http://www.tug.org/mactex/) using

```python
brew install --cask mactex-no-gui
```

or download simple small [BasicTex](http://www.tug.org/mactex/morepackages.html)

If you chose the latter, make sure to install these using
```python
sudo tlmgr install amsmath babel-english cbfonts-fd cm-super ctex doublestroke dvisvgm everysel
fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin
mathastext microtype ms physics preview ragged2e relsize rsfs
setspace standalone tipa wasy wasysym xcolor xetex xkeyval
```

After all this head over to [First Test File](https://github.com/MonitSharma/animation/blob/main/test1.py) to learn how to write simple code for Manim.
or you can take a look at the [Jupyter File](https://github.com/MonitSharma/animation/blob/main/tutorial1.ipynb) to run it in Jupyter environment.
