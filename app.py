from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    result = None
    from_scale = ""
    to_scale = ""
    temp_value = ""
    
    if request.method == 'POST':
        try:
            temp_value = float(request.form['temperature'])
            from_scale = request.form['from_scale']
            to_scale = request.form['to_scale']
            
            result = convert_temperature(temp_value, from_scale, to_scale)
            
        except ValueError:
            result = "Ошибка: введите корректное число"
    
    return render_template('convert.html', 
                         result=result,
                         from_scale=from_scale,
                         to_scale=to_scale,
                         temp_value=temp_value)

def convert_temperature(value, from_scale, to_scale):
    # Конвертируем в Цельсий
    if from_scale == "celsius":
        celsius = value
    elif from_scale == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_scale == "kelvin":
        celsius = value - 273.15
    else:
        return None
    
    # Конвертируем из Цельсия
    if to_scale == "celsius":
        return celsius
    elif to_scale == "fahrenheit":
        return celsius * 9/5 + 32
    elif to_scale == "kelvin":
        return celsius + 273.15
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5000)