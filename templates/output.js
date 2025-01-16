<script>
document.getElementById('contactform').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form values
    const firstname = document.querySelector('input[name="firstname"]').value;
    const lastname = document.querySelector('input[name="lastname"]').value;
    const email = document.querySelector('input[name="email"]').value;
    const message = document.querySelector('textarea[name="message"]').value;

    // Simulate form submission (you can replace this with actual form submission logic)
    setTimeout(() => {
        // Display output message
        const outputDiv = document.getElementById('form-output');
        outputDiv.textContent = `Thank you, ${firstname} ${lastname}. Your message has been received.`;
    }, 500); // Simulate a delay for form submission
});
</script>