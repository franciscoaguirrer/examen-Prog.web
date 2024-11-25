from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos para Ejercicio 2
users = {
    "juan": "admin",
    "pepe": "user"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        cans = int(request.form["cans"])
        price_per_can = 9000
        total_price = cans * price_per_can
        discount_rate = 0
        discount_amount = 0

        # CalculO de descuento según edad
        if 18 <= age <= 30:
            discount_rate = 0.15
        elif age > 30:
            discount_rate = 0.25

        # Calculo de monto de descuento y total con descuento
        discount_amount = total_price * discount_rate
        total_with_discount = total_price - discount_amount

        return render_template("ejercicio1.html",
                               name=name,
                               total_price=total_price,
                               discount_amount=discount_amount,
                               total_with_discount=total_with_discount,
                               age=age, cans=cans)
    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            if username == "juan":
                message = f"Bienvenido administrador {username}"
            else:
                message = f"Bienvenido usuario {username}"
        else:
            message = "Usuario o contraseña incorrectos"
        return render_template("ejercicio2.html", message=message)
    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
