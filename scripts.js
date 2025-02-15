// Add Progress Report
document.getElementById('progress-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get form values
    const date = document.getElementById('date').value;
    const timeSpent = document.getElementById('time-spent').value;
    const tasksCompleted = document.getElementById('tasks-completed').value;

    // Create report element
    const reportDiv = document.createElement('div');
    reportDiv.classList.add('report-item');
    reportDiv.innerHTML = `
        <p><strong>Date:</strong> ${date}</p>
        <p><strong>Time Spent:</strong> ${timeSpent} hours</p>
        <p><strong>Tasks Completed:</strong> ${tasksCompleted}</p>
    `;

    // Append to report list
    document.getElementById('report-list').appendChild(reportDiv);

    // Reset form
    document.getElementById('progress-form').reset();
});

// Handle Contact Form Submission (Optional)
document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thank you for reaching out!');
    document.getElementById('contact-form').reset();
});