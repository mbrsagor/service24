$(function () {
    "use strict";
    // ==============================================================
    // Product Sales
    // ==============================================================

    new Chartist.Bar('.ct-chart-product', {
        labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
        series: [
            [800000, 1200000, 1400000, 1300000, 1400000, 300000],
            [200000, 400000, 500000, 300000, 200000, 400000],
            [100000, 200000, 400000, 600000, 1200000, 1400000]
        ]
    }, {
        stackBars: true,
        axisY: {
            labelInterpolationFnc: function (value) {
                return (value / 1000) + 'k';
            }
        }
    }).on('draw', function (data) {
        if (data.type === 'bar') {
            data.element.attr({
                style: 'stroke-width: 40px'
            });
        }
    });
});

