from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for


def form(request):
    return render(request,'Form.html')


# Create your views here.


app = Flask(__name__)

# Sample data for branches
districts  = {
    "Ernakulam": ["Aluva", "Edapally", "Kalamasherry"],
    "Palakkad": ["Kollengode", "Nenmara", "Pattambi"],
    "Kozhikode": ["Aredathupalam", "mukkam", "Olavana"],
    "Thrissur": ["Athirappilly", "Thiruvambadi", "Chavakkad"],
    "Kottayam": ["Cheriyapally","Kumaranalloor","Kumarakom"],

    # Add more districts as needed
}



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        district = request.form.get('district')
        branch = request.form.get('branch')
        message = 'Application accepted'

        # Process the registration data (you may want to save it to a database)

        return render_template('Form.html', message=message)

    return render_template('Form.html', districts=districts.keys())



if __name__ == '__main__':
    app.run(debug=True)
