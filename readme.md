# Employee Registration System

### Database Configuration (Local)
To connect this project to your local Oracle Database:

1. Open `myproject/settings.py`.
2. Locate the `DATABASES` section.
3. Update the following fields with your local Oracle credentials:
   - `USER`: Your Oracle username
   - `PASSWORD`: Your Oracle password
   - `HOST`: Your local host (usually `localhost`)
   - `PORT`: Port (usually `1521`)
   - `NAME`: Your Oracle SID or Service Name (e.g., `xe` or `orcl`)

### Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Run server: `python manage.py runserver`
