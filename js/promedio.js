function promedio() {
    var porcentaje1 = verificar("porcentaje1");
    var porcentaje2 = verificar("porcentaje2");
    var porcentaje3 = verificar("porcentaje3");
    var porcentaje4 = verificar("porcentaje4");
    var porcentaje5 = verificar("porcentaje5");
    var porcentaje6 = verificar("porcentaje6");
    var porcentaje7 = verificar("porcentaje7");
    var porcentaje8 = verificar("porcentaje8");
    var porcentaje9 = verificar("porcentaje9");
    var porcentaje10 = verificar("porcentaje10");
    var pControl = verificar("pControl");
  
    var nota1 = verificar("nota1");
    var nota2 = verificar("nota2");
    var nota3 = verificar("nota3");
    var nota4 = verificar("nota4");
    var nota5 = verificar("nota5");
    var nota6 = verificar("nota6");
    var nota7 = verificar("nota7");
    var nota8 = verificar("nota8");
    var nota9 = verificar("nota9");
    var nota10 = verificar("nota10");
    var promedioControl = verificar("promedioControl");
  
    var promedio = document.getElementById("total").value =
      (parseInt(nota1) * (parseInt(porcentaje1) / 100)) +
      (parseInt(nota2) * (parseInt(porcentaje2) / 100)) +
      (parseInt(nota3) * (parseInt(porcentaje3) / 100)) +
      (parseInt(nota4) * (parseInt(porcentaje4) / 100)) +
      (parseInt(nota5) * (parseInt(porcentaje5) / 100)) +
      (parseInt(nota6) * (parseInt(porcentaje6) / 100)) +
      (parseInt(nota7) * (parseInt(porcentaje7) / 100)) +
      (parseInt(nota8) * (parseInt(porcentaje8) / 100)) +
      (parseInt(nota9) * (parseInt(porcentaje9) / 100)) +
      (parseInt(nota10) * (parseInt(porcentaje10) / 100)) +
      (parseInt(promedioControl) * (parseInt(pControl) / 100));
  
    var nExamen = verificar("nExamen");
    var pExamen = verificar("pExamen");
  
    var notaUno = promedio * (100 - parseInt(pExamen)) / 100;
  
    document.getElementById("pFinal").value =
      (parseInt(nExamen) * parseInt(pExamen) / 100) + notaUno;
  
    var pPresenta = (100 - parseInt(pExamen)) / 100;
    var pExamenListo = parseInt(pExamen) / 100;
    var parte1 = 40 - parseInt(pPresenta) * parseInt(promedio);
  
    document.getElementById("notaQueNecesito").value =
      (40 - (pPresenta * promedio)) / pExamenListo;
  }