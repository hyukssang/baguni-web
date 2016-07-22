# baguni-web

Steps for running the Python parse server:
  1. Set up Python virtual environment using 'virtualenv', activate it
  2. Using Python pip package manager, download the following:
      - beautifulsoup4 (not BeautifulSoup)
      - Flask
      - Flask-MySQL
      - requests
  3. Download MySQL, run the server
     (Optional) You may need to create a table called 'Baguni' and run init.sql inside sql folder
                This is for running the web app made with Flask only
