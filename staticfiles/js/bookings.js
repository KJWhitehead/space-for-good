/*jshint esversion: 6 */
const deleteButtons = document.getElementsByClassName("delete-btn");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();

        let bookingId = e.target.getAttribute("data-booking");

        fetch(`/facilities/bookings/${bookingId}/delete/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    console.log('Booking deleted successfully.');
                    location.reload();
                } else {
                    console.error('Failed to delete booking.');
                }
            })
            .catch(error => {
                console.error('Network error:', error);
            });
    });
}