import os

from flask import Flask, session
from flask import Flask, render_template, request
from flask_session import Session


#######################################################################
#App configurations
#######################################################################
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    Session(app)
    app.config['SESSION_TYPE'] = 'filesystem'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
#######################################################################
#App configurations ended
#######################################################################


#######################################################################
#Classic Mode
####################################################################
    #Home Page
    @app.route('/')
    def index():
        session['score'] = 0
        #First Question

        return render_template('index.html')

    #######################################################################
    #This function is the way you will change your score
    #The texts are going to be the text that will be shown in the next screen
    def button_clicking(intro_text, a_text,b_text,c_text, print_message_for_debug):
        print("##################################")
        if request.method == "POST":
            print("You sent a post request")
            if request.form.get("submit_a"):
                session['score'] = session['score']+1
                print('User should have selected a')

            elif request.form.get("submit_b"):
                session['score'] = session['score']+2
                print('User should have selected b')

            elif request.form.get("submit_c"):
                session['score'] = session['score']+3
                print('User should have selected c')

            else:
                print("MAJOR ISSUE!! User choice was neither a,b, or c")
                pass

            session['intro_text'] = intro_text
            session['choice_a_text'] = a_text
            session['choice_b_text'] = b_text
            session['choice_c_text'] = c_text
            print('message: ', print_message_for_debug)
            print('new score: ', session['score'])
            
        else:
            print("MAJOR ERROR IN BUTTON CLICK FUNCTION IF NOT GOING INTO THE FIRST ROUND")
            print("If you did get this message you sent a get request instead of a post request")
        print("##################################")


    #######################################################################
    #1st Question function
    @app.route("/classic_mode_q1",methods=['GET', 'POST'])
    def first_question():
        session['intro_text'] = "You fell asleep in the library and you suddenly find yourself late to Miss Misa's class! What are you going to do!?"
        session['choice_a_text'] = 'Start running to class'
        session['choice_b_text'] = 'Keep sleeping'
        session['choice_c_text'] = 'Roam the hallway'
        message = 'Classic Mode was selected'
        next_page = '/classic_mode_q2'

        button_clicking(session['intro_text'], session['choice_a_text'], session['choice_b_text'], session['choice_c_text'], message)
        
        return render_template('classic_mode.html', intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text'], pg_u_goto_after_clicked = next_page) 

    #######################################################################
    #2nd Question function
    @app.route("/classic_mode_q2", methods=['GET','POST'])    
    def second_question():

        new_intro_text =  "Mr. Seney sees you running in the hallway..!!!."
        new_a_text = "Speed up! Hope he doesn't catch me!!"
        new_b_text = 'Stop... slow down and walk'
        new_c_text = 'Wave and smile as you fast walk past him.'
        message = 'User just answered Q1'
        next_page = '/classic_mode_q3'

        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, message)
        return render_template('classic_mode.html', intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text'], pg_u_goto_after_clicked = next_page ) 
      
    #######################################################################
    #3rd Question function
    @app.route("/classic_mode_q3", methods=['GET','POST'])
    def third_question():

        new_intro_text =  'Your friends call you asking where you are at...'
        new_a_text = "You tell them to not worry about it!"
        new_b_text = 'Slowly start walking to class'
        new_c_text = 'Try to meet them in the lunch room'
        message = 'User just answered Q2'
        next_page = '/classic_mode_q4'

        
        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, message)
        return render_template('classic_mode.html', intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text'], pg_u_goto_after_clicked = next_page) 

    #######################################################################
    #4th Question function
    @app.route("/classic_mode_q4", methods=['GET','POST'])
    def fourth_question():

        new_intro_text =  "Mrs. Durbin finds you!? Now what!?"
        new_a_text = 'RUUUNNNN!!!'
        new_b_text = 'Smile and wave????'
        new_c_text = 'Try to make small talk'
        message = 'User just answered Q3'
        next_page = '/classic_mode_q5'

        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, message)
        
    
        return render_template('classic_mode.html', intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text'], pg_u_goto_after_clicked = next_page) 

    #######################################################################
    #5th Question function 
    @app.route("/classic_mode_q5", methods=['GET','POST'])
    def fifth_question():
        score = session['score']
        new_intro_text =  'Someone hands you a squishy and tells you to hide it'
        new_a_text = 'Ignore them and keep heading to class'
        new_b_text = "Run to hide it in Mr. Seney's office"
        new_c_text = 'Take it and head back to the library'
        message = 'User just answered Q4'
        next_page = '/end_screen/'
        
        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, message)
        return render_template('classic_mode.html', intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text'], pg_u_goto_after_clicked = next_page)

    #######################################################################
    #Classic Mode End Screen
    @app.route("/end_screen/", methods=['POST'])
    def ending():
        button_clicking('', '', '', '', 'Answered Q5 and below will be the final score')  
        score = session['score']
        print('Final score: ', score)
        if score < 6:
            last_scene = render_template('end_screen.html', ending_text = 'Sorry, you got in trouble anyway...')
        elif score == 7 or score == 9 or score == 11:
            last_scene = render_template('end_screen.html', ending_text = 'I have no idea but you escaped!!!!')
        else:
            last_scene = render_template('end_screen.html', ending_text = "Uhhh.. You just got yourself suspended...")

        print("##################################")
        return last_scene
#######################################################################
#Classic mode ended
#######################################################################



#######################################################################
#Create session & run the application
    sess = Session()
    sess.init_app(app)

    return app








#helpful websites
#https://stackoverflow.com/questions/15557392/how-do-i-display-images-from-google-drive-on-a-website
#https://unsplash.com/images/stock/blogging
#https://getbootstrap.com/docs/3.3/components/#btn-groups
#https://www.w3schools.com/bootstrap/bootstrap_theme_me.asp
#https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event