from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])

def main():
    # When it is a GET
    if request.method == "GET":
        return render_template("index.html")
    
    # When it is a POST (user has submitted your form)
    elif request.method == "POST":
        dp = request.form["provider"]

        ''' Alternatively, you can use 
            
            dp = request.values.get("provider")

            I prefer it because this way, I can provide a 
            default value in case the form parameter has no value i.e

            dp = request.values.get("provider", "default provider")
        '''
        

        dp_lower_case = dp.lower()

        return print(dp_lower_case)


