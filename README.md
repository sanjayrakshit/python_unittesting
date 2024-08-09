# pytest

Watch this [youtube video](https://www.youtube.com/watch?v=cHYq1MRoyI0&ab_channel=freeCodeCamp.org), the entire code base is just a walk through of whatever is shown in the video.

To get a better sense of setup and teardown using fixtures(preferred) check this [blog](https://pytest-with-eric.com/pytest-best-practices/pytest-setup-teardown/) out, and the [github repo](https://github.com/Pytest-with-Eric/pytest-setup-teardown-example) associated with it

It's really simple. Don't worry about it, if you don't understand. Just rewatch the video in 1.5x speed and you'll recall everything. 

### Commands to run test

```shell
pytest # runs all
pytest -v -s # runs in verbose and uses setup from class based testing
pytest -vs -m 'not slow' # verbose + setup + ignores tests that are marked slow


# With coverage and coverage report
coverage run -m pytest -vs -m 'not slow' && coverage report -m
coverage html # Generates beautified html file for test report
```
