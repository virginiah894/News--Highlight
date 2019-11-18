from flask import render_template
from app import app

@app.errorhandler(404)
def error_page(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('errorpage.html'),404
