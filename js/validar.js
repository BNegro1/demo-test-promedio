function validar() {
    var p1 = verificar("porcentaje1");
    var p2 = verificar("porcentaje2");
    var p3 = verificar("porcentaje3");
    var p4 = verificar("porcentaje4");
    var p5 = verificar("porcentaje5");
    var p6 = verificar("porcentaje6");
    var p7 = verificar("porcentaje7");
    var p8 = verificar("porcentaje8");
    var p9 = verificar("porcentaje9");
    var p10 = verificar("porcentaje10");
    var pC = verificar("pControl");
  
    document.getElementById("totalPorcentajes").value =
      parseInt(p1) +
      parseInt(p2) +
      parseInt(p3) +
      parseInt(p4) +
      parseInt(p5) +
      parseInt(p6) +
      parseInt(p7) +
      parseInt(p8) +
      parseInt(p9) +
      parseInt(p10) +
      parseInt(pC);
  
    var totalPorcentajes = document.getElementById("totalPorcentajes");
  
    if (totalPorcentajes.value > 100) {
      alert("Has sobrepasado el 100%");
      obj.style.borderColor = "#808080";
      return value;
    } else {
    }
  }
  
  function verificar(id) {
    var obj = document.getElementById(id);
    if (obj.value == "") value = "0";
    else value = obj.value;
    if (validate_importe(value)) {
      obj.style.borderColor = "#808080";
      return value;
    } else {
      obj.style.borderColor = "#f00";
      return 0;
    }
  }
  
  function validate_importe(value, decimal) {
    if (decimal == undefined) decimal = 0;
  
    if (decimal == 1) {
      var patron = new RegExp("^[0-9]+((,|\.)[0-9]{1,2})?$");
    } else {
      var patron = new RegExp("^([0-9])*$");
    }
  
    if (value && value.search(patron) == 0) {
      return true;
    }
    return false;
  }