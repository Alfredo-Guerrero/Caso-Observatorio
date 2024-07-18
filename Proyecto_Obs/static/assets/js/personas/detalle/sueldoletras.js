function calcularTotalYLetras() {
    var cantidad = parseFloat(document.getElementById('cantidad').value);
    var importe = parseFloat(document.getElementById('importe').value);
    var total = cantidad * importe;
    document.getElementById('total').value = total.toFixed(2);

    // Convertir el total a letras y mostrarlo en el campo de letras
    var letras = NumToWords(total);
    document.getElementById('letras').value = letras;
}

function NumToWords(num) {
    var units = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"];
    var tens = ["", "Diez", "Veinte", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"];
    var teens = ["Diez", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciséis", "Diecisiete", "Dieciocho", "Diecinueve"];
    var tempStr = "";
    var result = "";
    var decimalPart = "";

    var wholePart = Math.floor(num);
    var decPart = Math.round((num - wholePart) * 100);

    if (wholePart < 1000000000) {
        tempStr = "";

        // Miles
        if (Math.floor(wholePart / 1000) > 0) {
            if (wholePart === 1000) {
                tempStr += "Mil";
            } else if (wholePart < 2000 && wholePart > 1000) {
                tempStr += "Mil ";
            } else if (wholePart >= 2000 && wholePart < 3000) {
                tempStr += "Dos mil ";
            } else if (wholePart >= 3000 && wholePart < 4000) {
                tempStr += "Tres mil ";
            } else if (wholePart >= 4000 && wholePart < 5000) {
                tempStr += "Cuatro mil ";
            } else if (wholePart >= 5000 && wholePart < 6000) {
                tempStr += "Cinco mil ";
            } else if (wholePart >= 6000 && wholePart < 7000) {
                tempStr += "Seis mil ";
            } else if (wholePart >= 7000 && wholePart < 8000) {
                tempStr += "Siete mil ";
            } else if (wholePart >= 8000 && wholePart < 9000) {
                tempStr += "Ocho mil ";
            } else if (wholePart >= 9000 && wholePart < 10000) {
                tempStr += "Nueve mil ";
            } else if (wholePart >= 10000 && wholePart < 11000) {
                tempStr += "Diez mil ";
            } else if (wholePart >= 11000 && wholePart < 12000) {
                tempStr += "Once mil ";
            } else if (wholePart >= 12000 && wholePart < 13000) {
                tempStr += "Doce mil ";
            } else if (wholePart >= 1300 && wholePart < 14000) {
                tempStr += "Trece mil ";
            } else if (wholePart >= 14000 && wholePart < 15000) {
                tempStr += "Catorcce mil ";
            } else if (wholePart >= 15000 && wholePart < 16000) {
                tempStr += "Quince mil ";
            } else if (wholePart >= 16000 && wholePart < 17000) {
                tempStr += "Dieciseis mil ";
            } else if (wholePart >= 17000 && wholePart < 18000) {
                tempStr += "Diecisiete mil ";
            } else if (wholePart >= 18000 && wholePart < 19000) {
                tempStr += "Dieciocho mil ";
            } else if (wholePart >= 19000 && wholePart < 20000) {
                tempStr += "Diecinueve mil ";
            } else if (wholePart >= 20000 && wholePart < 30000) {
                tempStr += "Veinte mil ";
            } else if (wholePart >= 30000 && wholePart < 40000) {
                tempStr += "Treinta mil ";
            } else if (wholePart >= 40000 && wholePart < 50000) {
                tempStr += "Cuarenta mil ";
            } else if (wholePart >= 50000 && wholePart < 60000) {
                tempStr += "Cincuenta mil ";
            } else if (wholePart >= 60000 && wholePart < 70000) {
                tempStr += "Sensenta mil ";
            } else if (wholePart >= 70000 && wholePart < 80000) {
                tempStr += "Setenta mil ";
            } else if (wholePart >= 80000 && wholePart < 90000) {
                tempStr += "Ochenta mil ";
            } else if (wholePart >= 90000 && wholePart < 100000) {
                tempStr += "Noventa mil ";
            } else if (wholePart >= 100000 && wholePart < 200000) {
                tempStr += "Cien mil ";
            } else if (wholePart >= 200000 && wholePart < 300000) {
                tempStr += "Doscientos mil ";
            } else if (wholePart >= 300000 && wholePart < 400000) {
                tempStr += "Trescientos mil ";
            } else if (wholePart >= 400000 && wholePart < 500000) {
                tempStr += "Cuatrocientos mil ";
            } else if (wholePart >= 500000 && wholePart < 600000) {
                tempStr += "Quinientos mil ";
            } else if (wholePart >= 600000 && wholePart < 700000) {
                tempStr += "Seiscientos mil ";
            } else if (wholePart >= 700000 && wholePart < 800000) {
                tempStr += "Setecientos mil ";
            } else if (wholePart >= 800000 && wholePart < 900000) {
                tempStr += "Ochocientos mil ";
            } else if (wholePart >= 900000 && wholePart < 1000000) {
                tempStr += "Novecientos mil ";
            } else {
                tempStr += NumToWords(Math.floor(wholePart / 1000)) + " mil ";
            }
            wholePart %= 1000;
        }

        // Centenas
        if (Math.floor(wholePart / 100) > 0) {
            if (wholePart === 100) {
                tempStr += "Cien ";
            } else if (wholePart < 200 && wholePart > 100) {
                tempStr += "Ciento ";
            } else if (wholePart >= 200 && wholePart < 300) {
                tempStr += "Doscientos ";
            } else if (wholePart >= 300 && wholePart < 400) {
                tempStr += "Trescientos ";
            } else if (wholePart >= 400 && wholePart < 500) {
                tempStr += "Cuatrocientos ";
            } else if (wholePart >= 500 && wholePart < 600) {
                tempStr += "Quinientos ";
            } else if (wholePart >= 600 && wholePart < 700) {
                tempStr += "Seiscientos ";
            } else if (wholePart >= 700 && wholePart < 800) {
                tempStr += "Setecientos ";
            } else if (wholePart >= 800 && wholePart < 900) {
                tempStr += "Ochocientos ";
            } else if (wholePart >= 900 && wholePart < 1000) {
                tempStr += "Novecientos ";
            } else {
                tempStr += units[Math.floor(wholePart / 100)] + "cientos ";
            }
            wholePart %= 100;
        }

        // Decenas y unidades
        if (wholePart >= 10 && wholePart <= 19) {
            tempStr += teens[wholePart % 10];
        } else {
            if (Math.floor(wholePart / 10) > 0) {
                if (Math.floor(wholePart / 10) === 2 && wholePart % 10 > 0) {
                    tempStr += "Veinti";
                } else {
                    tempStr += tens[Math.floor(wholePart / 10)];
                    if (wholePart % 10 > 0) {
                        tempStr += " y ";
                    }
                }
            }
            if (wholePart > 0) {
                if (wholePart === 1 && tempStr === "") {
                    tempStr += "un";
                } else {
                    tempStr += units[wholePart % 10];
                }
            }
        }

        if (tempStr !== "") {
            if (wholePart === 1 && tempStr === "un") {
                result = tempStr;
            } else {
                result = tempStr;
            }
        }
    } else {
        result = "Sin cálculo de Rango";
    }

    if (decPart > 0) {
        if (result !== "") {
            result += " con ";
        }
        result += decPart + "/100";
    } else {
        result += " con 00/100";
    }

    if (wholePart === 1 && tempStr === "un") {
        result += " Nuevo Sol";
    } else {
        result += " Nuevos Soles";
    }

    return result;
}

// Llamar a la función calcularTotalYLetras() cuando se cargue la página
window.onload = function() {
    calcularTotalYLetras();
};

// Escuchar los cambios en los campos de cantidad y sueldo
document.getElementById('cantidad').addEventListener('input', calcularTotalYLetras);
document.getElementById('importe').addEventListener('input', calcularTotalYLetras);