# WebAppForNotes
Web application for creating and managing your notes.

## Installation

1. Clone repository
   
   `git clone https://github.com/MarcinOrl/WebAppForNotes.git`
   
3. Change directory
   
   `cd WebAppForNotes`
   
5. Create virtual environment
   
   `python -m venv venv`
   
   `venv\Scripts\activate (Windows)`
   
   `source venv/bin/activate (macOS/Linux)`
   
7. Install requirements
   
   `pip install -r requirements.txt`
   
9. Install npm dependencies
    
   `npm install`

11. Change directory
    
      `cd notes_project`
   
13. Migrate the DB

      `python manage.py migrate`
   
14. Run django server

      `python manage.py runserver`
