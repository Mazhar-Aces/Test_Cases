var data = [{
    type:'scattermapbox',
    lat:['45.5017'],
    lon:['-73.5673'],
    mode:'markers',
    marker: {
      size:14
    },
    text:['Montreal']
  }]
  
  var layout = {
    autosize: true,
    hovermode:'closest',
    mapbox: {
      bearing:0,
      center: {
        lat:45,
        lon:-73
      },
      pitch:0,
      zoom:5
    },
  }
  
  Plotly.setPlotConfig({
    mapboxAccessToken: "your access token"
  })
  
  Plotly.newPlot('myDiv', data, layout)
  