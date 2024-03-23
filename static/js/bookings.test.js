// @jest - environment jsdom

const {
    test,
    expect
} = require("@jest/globals");
const {
    deleteButtons
} = require("../js/bookings");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

test("delete button click event", () => {
    // Mock fetch function
    global.fetch = jest.fn(() =>
        Promise.resolve({
            ok: true,
            json: () => Promise.resolve()
        })
    );

    // Mock location.reload
    const originalReload = location.reload;
    location.reload = jest.fn();

    // Simulate click event on each delete button
    for (let button of deleteButtons) {
        button.click();

        // Check if fetch is called with the correct URL
        expect(fetch).toHaveBeenCalledWith(`/facilities/bookings/${button.getAttribute("data-booking")}/delete/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Check if location.reload is called after successful fetch
        expect(location.reload).toHaveBeenCalled();

        // Reset mocks
        jest.clearAllMocks();
    }

    // Restore original reload function
    location.reload = originalReload;
});