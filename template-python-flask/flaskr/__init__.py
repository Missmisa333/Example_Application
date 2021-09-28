import os

from flask import Flask
from flask import Flask, render_template, request



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

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

    @app.route('/')
    def index():
        return render_template('index.html')



    @app.route("/classic_mode")
    def original():
        intro_text = "You fell asleep in the library and you suddenly find yourself late to Miss Misa's class! What are you going to do!?"
        a = 'Start running to class'
        b = 'Keep sleeping'
        c = 'Roam the hallway'
        return render_template('classic_mode.html', intro = intro_text, a_text = a, b_text = b, c_text = c) 
                          

    @app.route("/choice_a/", methods=['POST'])
    def choosing_a():
        intro_text = "Mr. Seney sees you running in the hallway..."
        a = "Speed up! Hope he doesn't catch me!!"
        b = 'Stop... slow down and walk'
        c = 'Wave and smile as you fast walk past him.'
        
        return render_template('classic_mode_r2.html', intro=intro_text, a_text = a, b_text = b, c_text = c)


    @app.route("/choice_b/", methods=['POST'])
    def choosing_b():
        intro_text = "Your friends call you asking where you are at..."
        a = 'You tell them to not worry about it'
        b = 'Slowly start walking to class'
        c = 'Try to meet them in the lunch room'
        
        return render_template('classic_mode_r2.html', intro=intro_text, a_text = a, b_text = b, c_text = c)

    @app.route("/choice_c/", methods=['POST'])
    def choosing_c():
        intro_text = 'Someone hands you a squishy and tells you to hide it'
        a = 'Ignore them and keep heading to class'
        b = "Run to hide it in Mr. Seney's office"
        c = 'Take it and head back to the library'
        
        return render_template('classic_mode_r2.html', intro=intro_text, a_text = a, b_text = b, c_text = c)

    @app.route("/choice_a2/", methods=['POST'])
    def choosing_a2():
        intro_text = "OH NO!!! Mr.Seney caught you..."
        a = 'Try to bribe him with kiss chocolates'
        b = 'Apologize and run away'
        c = 'Pretend to cry and go to class'
        
        return render_template('classic_mode_r3.html', intro=intro_text, a_text = a, b_text = b, c_text = c)

    @app.route("/choice_b2/", methods=['POST'])
    def choosing_b2():
        intro_text = "Mrs. Durbin finds you!? Now what!?"
        a = 'RUUUNNNN!!!'
        b = 'Smile and wave????'
        c = 'Try to make small talk'
        
        return render_template('classic_mode_r3.html', intro=intro_text, a_text = a, b_text = b, c_text = c)

    @app.route("/choice_c2/", methods=['POST'])
    def choosing_c2():
        intro_text = "You run right into Miss Misa"
        a = 'Pretend your sick'
        b = 'Escape from the school'
        c = 'Give her a fake pass'
        
        return render_template('classic_mode_r3.html', intro=intro_text, a_text = a, b_text = b, c_text = c)

    @app.route("/end_screen/", methods=['POST'])
    def ending():  
        return render_template('end_screen.html')


    # register the database commands
    from flaskr import db

    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app








#helpful websites
#https://stackoverflow.com/questions/15557392/how-do-i-display-images-from-google-drive-on-a-website
#https://unsplash.com/images/stock/blogging
#https://getbootstrap.com/docs/3.3/components/#btn-groups
#https://www.w3schools.com/bootstrap/bootstrap_theme_me.asp
#https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event