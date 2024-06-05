# WebAppForNotes
Web application for creating and managing your notes.

## Installation

1. Clone repository
   `git clone https://github.com/MarcinOrl/WebAppForNotes.git`
2. Change directory
   `cd WebAppForNotes`
3. Create virtual environment
   `python -m venv venv`
   `venv\Scripts\activate (Windows)`
   `source venv/bin/activate (macOS/Linux)`
5. Install requirements
   `pip install -r requirements.txt`
6. Install npm dependencies
   `npm install`
7. Change directory
   `cd notes_project`
8. Migrate the DB
   `python manage.py migrate`
9. Run django server
   `python manage.py runserver`
