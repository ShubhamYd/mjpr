  var output =""

  api_arima = "http://127.0.0.1:5000/api/arima?filename=microsoft"
  api_lstm = "http://127.0.0.1:5000/api/lstm?filename=microsoft"
  


// document.getElementById('pctchange').innerHTML = "popat";

fetch(api_arima)
      .then(response => response.json())
      .then(json => {
        var radr = json['Pctchange']
        document.getElementById('pctchange').innerHTML = radr;
        document.getElementById('average').innerHTML = json['avg'];
        document.getElementById('plus').innerHTML = json['pdiff'];
        document.getElementById('minus').innerHTML = json['ndiff'];
      });


fetch(api_lstm)
      .then(response => response.json())
      .then(json => {
        var radr = json['Close']
        document.getElementById('actprice').innerHTML = radr;
        document.getElementById('error').innerHTML = json['Error'];
        document.getElementById('predict').innerHTML = json['Predictions'];
        document.getElementById('risks').innerHTML = json['Risk'];
      });