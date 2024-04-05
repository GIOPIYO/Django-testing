// Get product details from URL parameters
const params = new URLSearchParams(window.location.search);
const productName = params.get('name');
const productDescription = params.get('description');
const productPrice = params.get('price');

// Populate product details on the page
document.getElementById('product-name').textContent = productName;
document.getElementById('product-description').textContent = productDescription;
document.getElementById('product-price').textContent = `Price: $${productPrice}`;

// Function to view product details
function viewProduct(name, description, price) {
    // Encode product details as URL parameters
    const params = new URLSearchParams({
        name: name,
        description: description,
        price: price
    });
    // Redirect to product page with URL parameters
    window.location.href = 'prodDetails?' + params.toString();
}

// Sample equipment data (replace with actual data)
const equipmentData = [
    { name: 'Tractor', description: 'A powerful and versatile tractor suitable for various farm tasks such as plowing, planting, and towing.', price: 50000 },
    { name: 'Combine Harvester', description: 'An advanced combine harvester designed to efficiently harvest crops like wheat, corn, and soybeans.', price: 150000 },
    {name: 'Seeder', description: 'A precision seeder ideal for planting seeds with accuracy and uniformity. Features adjustable seed rates and row spacing to accommodate different crop types and planting conditions.', price: 20000 },
    {name: 'Sprayer', description: 'A high-performance sprayer for applying fertilizers, herbicides, and pesticides to crops. Equipped with precision spraying technology and adjustable boom widths for efficient and targeted application.', price: 7000},
    {name: 'Plow', description: 'A heavy-duty plow for breaking up and turning over soil in preparation for planting. Designed to handle tough soil conditions and provide consistent depth and furrow shape', price: 20000},
    {name: 'Cultivator', description: 'A versatile cultivator for weed control and soil aeration. Features adjustable tines and depth settings to effectively manage weeds and improve soil structure.', price: 25000},
    {name: 'Livestock Trailer', description: 'A sturdy livestock trailer for transporting cattle, sheep, or other livestock. Designed with safety features and ample ventilation to ensure the well-being of animals during transportation.', price: 10000},
    {name: 'Hay Baler', description: 'A reliable hay baler for baling hay and straw with efficiency and consistency. Equipped with features such as automatic tying and bale density control for optimal bale quality.', price: 24000},
    {name: 'Grain Dryer', description: 'An efficient grain dryer for drying harvested grain to the desired moisture content. Equipped with advanced drying technology and temperature control for preserving grain quality.', price: 27000},
    {name:'Mower Conditioner', description: 'A versatile mower conditioner for cutting and conditioning hay or forage crops. Features adjustable cutting widths and conditioning settings to optimize crop drying and quality.', price: 15000},
    // Add more equipment data here
];

// Function to search for equipment
function searchEquipment() {
    const searchTerm = document.getElementById('search-input').value.toLowerCase();
    const filteredEquipment = equipmentData.filter(equipment => {
        return equipment.name.toLowerCase().includes(searchTerm) || equipment.description.toLowerCase().includes(searchTerm);
    });
    displayEquipment(filteredEquipment);
}

// Function to display equipment
function displayEquipment(equipment) {
    const equipmentList = document.getElementById('equipment-list');
    equipmentList.innerHTML = ''; // Clear previous results
    if (equipment.length === 0) {
        equipmentList.innerHTML = '<p>No equipment found.</p>';
    } else {
        equipment.forEach(item => {
            const equipmentItem = document.createElement('div');
            equipmentItem.classList.add('equipment-item');
            equipmentItem.innerHTML = `
                <h2>${item.name}</h2>
                <p>Description: ${item.description}</p>
                <p>Price: $${item.price}</p>
            `;
            equipmentList.appendChild(equipmentItem);
        });
    }
}