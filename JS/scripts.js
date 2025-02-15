<scripts>
  document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Completely stops the form from submitting anywhere
    
    // Display success message
    const successMessage = document.createElement('p');
    successMessage.textContent = "Message Successfully Received!";
    successMessage.style.color = "green";
    successMessage.style.fontWeight = "bold";
    successMessage.classList.add('success-message');
    
    // Remove old message if present
    const oldMessage = this.querySelector('.success-message');
    if (oldMessage) {
      oldMessage.remove();
    }
    
    // Append the message to the form
    this.appendChild(successMessage);
    
    // Clear the form fields
    this.reset();
  });
</scripts>
