function openModal(itemId) {
    // Fetch item details using the API
    fetch(`/api/items/${itemId}/`)
        .then(response => response.json())
        .then(data => {
            const modalBody = document.getElementById('modal-body');
            modalBody.innerHTML = `
                <img src="${data.image}" alt="${data.name}" class="modal-image">
                <h2>${data.name}</h2>
                <p>${data.description}</p>
                <h3>Sizes</h3>
                <ul>
                    ${data.sizes.map(size => `<li>${size.name}: $${size.price}</li>`).join('')}
                </ul>
            `;
            document.getElementById('item-modal').classList.remove('hidden');
        });
}

function closeModal() {
    document.getElementById('item-modal').classList.add('hidden');
}

// Smooth scrolling for links (optional)
document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
