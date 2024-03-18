const deleteButtons = document.getElementsByClassName("delete-btn");
const editButtons = document.querySelectorAll('.edit-btn');


editButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Redirect to the edit URL corresponding to the booking ID
        const bookingId = button.dataset.booking;
        window.location.href = `/facilities/bookings/${bookingId}/edit/`;
    });
});

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        // Prevent the default action of the button (e.g., form submission)
        e.preventDefault();

        // Retrieve the booking ID from the data-booking attribute of the button
        let bookingId = e.target.getAttribute("data-booking");

        // Send a DELETE request to the server to delete the booking
        fetch(`/facilities/bookings/${bookingId}/delete/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    // Optionally, handle success (e.g., update UI)
                    console.log('Booking deleted successfully.');
                    // Reload the page or update UI as needed
                    location.reload();
                } else {
                    // Optionally, handle error (e.g., display error message)
                    console.error('Failed to delete booking.');
                }
            })
            .catch(error => {
                // Optionally, handle network error
                console.error('Network error:', error);
            });
    });
}