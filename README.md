Open this project in your IDE of choice. You can either run it with a virtualenv or using the OS's Python compiler

1. Using a virtualenv in Conda (replace the **x** with your python version, **envname** with a name of your choice)

```
conda create -n envname python=x.x anaconda
```

2. Activate the virtualenv

```
conda activate envname
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Execute script

```
python main.py
```

5. Deactivating virtual env

```
conda deactivate
```

Or by simply using your OS's Python installation:

1. Open the project in your IDE of choice

2. Open a terminal

3. Install dependencies

```
pip install -r requirements.txt
```

4. Execute script

```
python main.py
```