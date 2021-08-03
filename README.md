# Distance Blueprint
Simple implementation of Flask's blueprint using [Yandex Map API](https://yandex.ru/dev/maps/) in order to calculate distance from an
specified address given as http request to the Moscow Ring Road ([MKAD](https://yandex.com/maps/213/moscow/geo/mkad/8059375/?from=api-maps&ll=37.606101%2C55.741845&origin=jsapi_2_1_79&pt=37.632206%2C55.898947&z=10)). Note: When address is inside MKAD, distance isn't calculated.


## Instructions to run
Clone the project
```sh
git clone git@github.com:NoriakiMawatari/distance_blueprint.git
```
Once located on the distance_blueprint directory, [pyenv](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/#how-to-install-pyenv)
and [poetry](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/#how-to-install-poetry) packages are needed to setup,

For Linux, the [pyenv-installer](https://github.com/pyenv/pyenv-installer) could be used:
```sh
curl https://pyenv.run | bash
```
```sh
# Restart shell so the path changes take effect.
exec $SHELL
```
It is recommended to install Poetry on a system level. Thus, for Linux, MacOS or WSL(Windows Subsystem for Linux):
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
```sh
# Run this command to apply changes for your current shell session.
source $HOME/.poetry/env
```


With the following command, a new virtual environment is created. Additionally, resolves and install dependencies.
```sh
poetry install
```
Make sure to activate the virtual environment,
```sh
source ~/.cache/pypoetry/virtualenvs/<name-of-venv>/bin/activate
```
In order to success using this blueprint an API token is needed, this developer key can be obtained for free upon registration [here](https://yandex.com/dev/maps/jsapi/doc/2.1/quick-start/index.html#get-api-key).

Then, creates a .env file in distance_blueprint directory and stores your API key as follows:
```sh
yandex_token = <your-api-key>
```
Finally, run:
```sh
python run.py
```

To visualize and interact with the blueprint visit [http://localhost:5000/](http://localhost:5000/)

Also, demo.log file stores results.

### Run tests
```shell
pytest .
```

In order to visualize each test instead of only displaying dots, you can run:
```sh
pytest . -v
```
