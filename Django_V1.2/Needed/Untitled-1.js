               <div class="form-row" style="margin-left: 42px;">
                    <!-- First Row: Product Name, Product Code, Quantity, Order Name -->
                    <div class="form-col">{{ form.product_name.label_tag }}<input type="text" id="id_product_name" name="product_name" class="dynamic-product-name"></div>
                    <div class="form-col">{{ form.product_code.label_tag }}{{ form.product_code }}</div>
                    <div class="form-col">{{ form.quantity.label_tag }}{{ form.quantity }}</div>
                </div> 

            <div id="additionalProducts">
                <!-- Container for additional product fields -->
                <div id="productButtons" style="display: distance-between; flex-direction: column; align-items: flex-start; margin-bottom:20px;" >
                    <button type="button" id="addProduct" class="btn btn-orange">Add product</button>
                    <button type="button" id="removeSelectedProducts" class="btn btn-red" style="margin-top: 10px; display: none;">Remove Selected</button>
                </div>
            </div>

            <script>
                document.getElementById('addProduct').addEventListener('click', function() {
                    const container = document.createElement('div');
                    container.className = 'form-row'; // Use the same class as the first row
            
                    // Generate a unique identifier for each row
                    const uniqueId = Date.now();
            
                    // Add a checkbox input for selecting the product row
                    container.innerHTML = `
                        <div>
                            <input type="checkbox" class="product-checkbox" id="checkbox_${uniqueId}">
                        </div>
                        <div class="form-col">
                            <label for="product_name_${uniqueId}">Product Name:</label>
                            <input type="text" id="product_name_${uniqueId}" name="products[${uniqueId}][name]" class="dynamic-product-name">
                        </div>
                        <div class="form-col">
                            <label for="product_code_${uniqueId}">Product Code:</label>
                            <input type="text" id="product_code_${uniqueId}" name="products[${uniqueId}][code]" class="dynamic-product-code">
                        </div>
                        <div class="form-col">
                            <label for="quantity_${uniqueId}">Quantity:</label>
                            <input type="number" id="quantity_${uniqueId}" name="products[${uniqueId}][quantity]" value="" class="dynamic-product-quantity">
                        </div>
                    `;
                    const additionalProducts = document.getElementById('additionalProducts');
                    additionalProducts.insertBefore(container, additionalProducts.children[0]); // Insert before the buttons
            
                    // Show the Remove Selected button when the first product is added
                    document.getElementById('removeSelectedProducts').style.display = 'inline-block';
            
                    setupAutocomplete(`#product_name_${uniqueId}`, `#product_code_${uniqueId}`, 'product');
                    setupAutocomplete(`#product_code_${uniqueId}`, `#product_name_${uniqueId}`, 'product');
                });
            
                document.getElementById('removeSelectedProducts').addEventListener('click', function() {
                    document.querySelectorAll('.product-checkbox:checked').forEach(checkbox => {
                        checkbox.closest('.form-row').remove();
                    });
            
                    // Hide the Remove Selected button if no more products are present
                    if (document.querySelectorAll('.product-checkbox').length === 0) {
                        document.getElementById('removeSelectedProducts').style.display = 'none';
                    }
                });
            
                function setupAutocomplete(elementId, otherElementId, searchType) {
                    $(elementId).autocomplete({
                        source: function(request, response) {
                            $.ajax({
                                url: searchType === 'product' ? "{% url 'product_search' %}" : "{% url 'project_search' %}",
                                dataType: "json",
                                data: {
                                    term: request.term,
                                    field: $(elementId).hasClass('dynamic-product-name') ? "name" : "code"
                                },
                                success: function(data) {
                                    // Filter out already selected products
                                    const usedProducts = $(".dynamic-product-name, .dynamic-product-code").map(function() {
                                        return this.value;
                                    }).get();
                                    const filteredData = data.filter(item => !usedProducts.includes(item.name) && !usedProducts.includes(item.code));
                                    response(filteredData);
                                },
                                error: function(xhr, status, error) {
                                    console.error("Error:", error);
                                }
                            });
                        },
                        select: function(event, ui) {
                            if ($(elementId).hasClass('dynamic-product-name')) {
                                $(elementId).val(ui.item.name);
                                $(otherElementId).val(ui.item.code);
                            } else {
                                $(elementId).val(ui.item.code);
                                $(otherElementId).val(ui.item.name);
                            }
                            return false;
                        }
                    });
                }
            </script>
        

            http://127.0.0.1:8000/orders/new/#