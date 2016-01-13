var {{name}} = c3.generate({
    bindto: '#{{name}}',
    size: {
      height: 480,
    },
    data: {
      x : 'x',
      url : '{{data_url}}',
      mimeType: 'json',
      type: 'bar'
    },
    axis: {
        x: {
            type: 'category', // this needed to load string x value
            height: 80
        },
        y: {
          label: '{{y_label}}'
        }
    },
    legend: {
      show: false
    }
});
