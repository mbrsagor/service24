
        // Add new line function
        function addField(node) {
            let line = node.parentNode.parentNode.cloneNode(true);
            document.getElementById('rows').appendChild(line);
        }
        // Remove line node function
        function removeField(node) {
            let row = node.parentNode.parentNode;
            row.parentNode.removeChild(row);
        }
        // Image upload show preview
        document.getElementById('files').onchange = function () {
            let src = URL.createObjectURL(this.files[0])
            document.getElementById('image').src = src
        }
        // Price on change
        function priceOnInput(){
            let price = document.getElementById("price").value;
            document.getElementById("amount").innerHTML = "$"+price;
        }

