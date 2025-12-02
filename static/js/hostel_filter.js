function filterHostels() {
    const priceFilter = document.getElementById("priceFilter").value;
    const locationFilter = document.getElementById("locationFilter").value.toLowerCase();
    const roomFilter = document.getElementById("roomFilter").value.toLowerCase();

    const hostelCards = document.querySelectorAll(".hostel-card");
    let anyVisible = false;

    hostelCards.forEach(card => {
        const price = parseInt(card.dataset.price);
        const location = card.dataset.location.toLowerCase();
        const room = card.dataset.room.toLowerCase();

        let show = true;

        // Price filter
        if (priceFilter) {
            if (priceFilter.includes("+")) {
                const min = parseInt(priceFilter);
                if (price < min) show = false;
            } else {
                const [min, max] = priceFilter.split("-").map(Number);
                if (price < min || price > max) show = false;
            }
        }

        // Location filter
        if (locationFilter && location !== locationFilter) show = false;

        // Room filter
        if (roomFilter && room !== roomFilter) show = false;

        card.style.display = show ? "block" : "none";
        if (show) anyVisible = true;
    });

    document.getElementById("noResults").classList.toggle("d-none", anyVisible);
}

function clearFilters() {
    document.getElementById("priceFilter").value = "";
    document.getElementById("locationFilter").value = "";
    document.getElementById("roomFilter").value = "";
    filterHostels();
}