# Dublin City Bridges · Quiz API

A Django REST Framework prototype for storing and serving bridge-related quiz content.

**Python · Django · Django REST Framework**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- Quiz models and serializers.
- API URL configuration.
- A SQLite-backed Django development project.

> **Project notes:** The project is inside backend/. No Python requirements file is committed; the settings header records Django 5.1.5 and the source imports Django REST Framework. The static Know Dublin frontend is a separate application.

## Getting started

Requires Python, pip and a virtual environment. Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/dublin-city-bridges-backend.git
cd dublin-city-bridges-backend
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

**Dependency setup is incomplete:** no requirements file is committed. Identify and install the dependencies imported by the project before continuing. The project is inside backend/. No Python requirements file is committed; the settings header records Django 5.1.5 and the source imports Django REST Framework. The static Know Dublin frontend is a separate application.

After resolving the project notes and configuring the local environment, use:

```bash
cd backend
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Repository guide

| Path | Purpose |
| --- | --- |
| [backend/manage.py](backend/manage.py) | Django management commands |
| [backend/backend/settings.py](backend/backend/settings.py) | Django configuration |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

No current hosted endpoint is established by this README. A backend deployment needs a configured runtime and its own service settings; GitHub Pages cannot execute the server-side application.

## Credits and reuse

Reuse terms are recorded in [LICENSE](LICENSE). Third-party assets and dependencies retain their own terms.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/dublin-city-bridges-backend/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#dublin-city-bridges--quiz-api)
